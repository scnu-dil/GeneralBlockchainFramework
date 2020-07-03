

pragma solidity ^0.4.24;

contract file{

    mapping(string => string) state;

    constructor() public{}

    function get(string UUID) constant public returns(string record){
        // try catch
        return state[UUID];
    }

    function set(string UUID, string json_record) public{
        state[UUID] = json_record;
    }
}






















































