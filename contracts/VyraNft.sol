// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VyraNft is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenId;
    uint256 public constant maxSupply = 16;
    uint256 public constant nftPrice = 8000000000000000;

    mapping(uint256 => string) public tokenIdToTokenURI;
    mapping(uint256 => address) public tokenIdToSender;
    event NewCollectibleMinted(uint256 indexed newTokenId);

    constructor() ERC721("Melbourne Collection", "VYRA") {}

    function createCollectible(string memory tokenURI)
        public
        payable
        returns (uint256)
    {
        require(_tokenId.current() < maxSupply);
        require(
            nftPrice == msg.value,
            "You have not supplied the correct amount of Ether!"
        );
        uint256 newTokenId = _tokenId.current();
        tokenIdToTokenURI[newTokenId] = tokenURI;

        _safeMint(msg.sender, newTokenId);
        _tokenId.increment();

        setTokenURI(newTokenId, tokenURI);
        tokenIdToSender[newTokenId] = msg.sender;

        emit NewCollectibleMinted(newTokenId);
        return newTokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
