

pragma solidity ^0.4.24;

contract TianwenKV{

    mapping(string => string) state;

    constructor() public{}

    function get(string item_element) constant public returns(string record){
        // try catch
        return state[item_element];
    }

    function set(string item_element, string json_record) public{
        state[item_element] = json_record;
    }
}



















































