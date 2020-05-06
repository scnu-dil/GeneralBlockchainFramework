

pragma solidity ^0.4.24;

contract traffic{

    address public trafficSender;

    struct s {
        string url;
        string hashvalue;
    }

    mapping(address => s) state;

    constructor() public{}

    function get() constant public returns(string url, string hashvalue){
        return (state[msg.sender].url, state[msg.sender].hashvalue);
    }

    function set(string _url, string _hashvalue) public{
        trafficSender = msg.sender;
        state[trafficSender].url = _url;
        state[trafficSender].hashvalue = _hashvalue;
    }
}









































