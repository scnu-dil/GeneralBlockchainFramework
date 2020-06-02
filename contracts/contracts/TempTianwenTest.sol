pragma solidity ^0.4.24;
pragma experimental ABIEncoderV2;
import "./Table.sol";


contract TianwenTest {
    event CreateResult(int count);
    event InsertResult(int count);


    // 拓展性不足的
    struct Record {
        string item_Element;
        string item_N_line;
        string item_O_XH;
        string item_O_XFe;
        string item_O_loge;

        string item_C_XH;
        string item_C_XFe;
        string item_C_loge;
    }


    //create table
    function create() public returns(int){
        TableFactory tf = TableFactory(0x1006); //The fixed address is 0x1010 for TableFactory
        //创建名为t_Tianwen_test的表，其中Element为主键，表中的列项如tem_Element,item_N_line,item_O_XH,item_O_XFe。。等
        int count = tf.createTable("t_Tianwen_test", "Element", "item_Element,item_N_line,item_O_XH,item_O_XFe,item_O_loge,item_C_XH,item_C_XFe,item_C_loge");
	      emit CreateResult(count);

	      return count;
    }

        //select records
    function select(string name) public constant returns(Record[]){
        TableFactory tf = TableFactory(0x1006);
        Table table = tf.openTable("t_Tianwen_test");
        Condition condition = table.newCondition();
        Entries entries = table.select(name, condition);

        //init

        Record[] memory records_list = new Record[](uint256(entries.size()));

        // for entries
        for(int i=0; i<entries.size(); ++i) {
            Entry entry = entries.get(i);

            records_list[uint256(i)].item_Element = entry.getString("item_Element");
            records_list[uint256(i)].item_N_line = entry.getString("item_N_line");
            records_list[uint256(i)].item_O_XH = entry.getString("item_O_XH");
            records_list[uint256(i)].item_O_XFe = entry.getString("item_O_XFe");

            records_list[uint256(i)].item_O_loge = entry.getString("item_O_loge");
            records_list[uint256(i)].item_C_XH = entry.getString("item_C_XH");
            records_list[uint256(i)].item_C_XFe = entry.getString("item_C_XFe");
            records_list[uint256(i)].item_C_loge = entry.getString("item_C_loge");
        }


        return records_list;
    }



    //insert records
    function insert(string item_Element, string item_N_line, string item_O_XH, string item_O_XFe, string item_O_loge, string item_C_XH, string item_C_XFe, string item_C_loge) public returns(int) {
        TableFactory tf = TableFactory(0x1006);
        Table table = tf.openTable("t_Tianwen_test");
        
        Entry entry = table.newEntry();

        entry.set("item_Element", item_Element);
        entry.set("item_N_line", item_N_line);
        entry.set("item_O_XH", item_O_XH);
        entry.set("item_O_XFe", item_O_XFe);

        entry.set("item_O_loge", item_O_loge);
        entry.set("item_C_XH", item_C_XH);
        entry.set("item_C_XFe", item_C_XFe);
        entry.set("item_C_loge", item_C_loge);
        
        int count = table.insert(item_Element, entry);
        emit InsertResult(count);
        
        return count;
    }

}
