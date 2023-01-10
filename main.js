var username = "";
var password = "";

function send()
{
    if ($ ("#input1").val() == username && $ ("#input2").val() == password)
    {
        $ ("#login-box").css("left", "-50%");
        $ ("#main-page").css("left", "50%");
    }
    else
    {
        alert("invalid username or password");
    }
}

function logout ()
{
    $ ("#main-page").css("left", "135%");  
    $ ("#login-box").css("left", "50%");
}

function addRecordPage ()
{
    $ ("#main-page").css("top", "150%");
    $ ("#add-record-page").css("top", "50%");
}

async function Add_data ()
{
    add_list = [
        $ ("#year-add-record").val(),
        $ ("#firstname-add-record").val(),
        $ ("#lastname-add-record").val(),
        $ ("#roll-add-record").val(),
        $ ("#age-add-record").val(),
        $ ("#gender-add-record").val(),
        $ ("#dept-add-record").val()]

    flag = 0
    if (add_list[0] == "--") {flag+=1;}
    if (add_list[1] == '') {flag+=1;}
    if (add_list[2] == '') {flag+=1;}
    if (add_list[3] == '') {flag+=1;}
    if (add_list[4] == '') {flag+=1;}
    if (add_list[5] == "--") {flag+=1;}
    if (add_list[6] == "--") {flag+=1;}
    
    if (!flag)
    {
        await eel.add_data(add_list)();
        alert("Saved ✔");
    }
    else
    {
        alert(flag + " invalid format in Input.");
    }
}

function Add_back ()
{
    $ ("#main-page").css("top", "50%");
    $ ("#add-record-page").css("top", "-150%");
}

function showExistingRecords ()
{
    $ ("#show-record-page").css("top", "50%");
    $ ("#main-page").css("top", "-150%");
}

function Show_back ()
{
    $ ("#show-record-page").css("top", "150%");
    $ ("#main-page").css("top", "50%");
}

var data;
var table_limit = 15;
var total_page;
var current_page = 0;
var row = 0;
async function showData (add_data_to_table, inc, get_data)
{
    if (get_data)
    {
        data_lis = [
            $ ("#year-show-record").val(),
            ($ ("#firstname-show-record").val() == "") ? "--" : $ ("#firstname-show-record").val(),
            ($ ("#lastname-show-record").val() == "") ? "--" : $ ("#lastname-show-record").val(),
            ($ ("#roll-show-record").val() == "") ? "--" : $ ("#roll-show-record").val(),
            ($ ("#age-show-record").val() == "") ? "--" : $ ("#age-show-record").val(),
            $ ("#gender-show-record").val(),
            $ ("#dept-show-record").val()]
    
        data = await eel.show_data(data_lis)();

        total_page = Math.ceil(data.length/table_limit);
        current_page = 0;
        }

    if (add_data_to_table)
    {
        if (current_page+inc <= total_page-1 && current_page+inc > -1)
        {
            if (!get_data && add_data_to_table)
            {
                for (let i = 0; i < table_limit; i++)
                {
                    $ ("#table-row").remove();
                }
            }
            current_page += inc;
            offset = table_limit * current_page;
            markup_start = "<tr id=\"table-row\">"
            markup_main = "";
            markup_end = "</tr>"
            console.log("Current_page ", current_page, ", Table_limit ", table_limit, ", data.length-(offset+1) ", data.length-offset);
            for (let row = offset; (row - offset) < table_limit && row <= data.length; row++)
            {
                markup_main += "<td class=\"cell-data\">" + data[row][2] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][0] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][1] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][3] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][4] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][5] + "</td>";
                markup_main += "<td class=\"cell-data\">" + data[row][6] + "</td>";

                $ ("table tbody").append(markup_start+markup_main+markup_end);
                markup_main = ""
            }
            row += table_limit;
        }
    }

    $ ("#show-record-page").css("left", "-135%");
    $ ("#table-content").css("left", "50%");
}

function Ok_button ()
{
    $ ("#show-record-page").css("left", "50%");
    $ ("#table-content").css("left", "150%");
}

function deleteExistingRecords ()
{
    $ ("#delete-record-page").css("left", "50%");
    $ ("#main-page").css("left", "-135%");
}

async function Delete ()
{
    delete_lis = [
        $ ("#year-delete-record").val(),
        ($ ("#firstname-delete-record").val() == "") ? "--" : $ ("#firstname-show-record").val(),
        ($ ("#lastname-delete-record").val() == "") ? "--" : $ ("#lastname-show-record").val(),
        ($ ("#roll-delete-record").val() == "") ? "--" : $ ("#roll-show-record").val(),
        ($ ("#age-delete-record").val() == "") ? "--" : $ ("#age-show-record").val(),
        $ ("#gender-delete-record").val(),
        $ ("#dept-delete-record").val()]

    pass = prompt("Enter admin password to delete any record.", "")
    if  (pass == password)
    {
        data = await eel.delete_data(delete_lis)();
        alert (data);
    }
    else
    {
        alert ("Wrong password, Operation failed.")
    }
}

function Delete_back ()
{
    $ ("#delete-record-page").css("left", "135%");
    $ ("#main-page").css("left", "50%");
}

async function clearData ()
{
    input_pass = prompt("Enter your password to continue...", "");
    if (input_pass == password)
    {
        msg = await eel.reset_database()();
        alert(msg);
    }
    else {alert("Wrong password, Operation failed.")}
}

var theme_array_num = 0;
let theme_array = [["#011a25", "#012536", "#ffb703"],
                   ["#2c7896", "#51b3e0", "#5f008b"],
                   ["#011a25", "#012536", "#ff6600"],
                   ["#8d8d8d", "#d3d3d3", "#ff6600"],
                   ["#000000", "#222222", "#ff6600"]]

function change_theme ()
{
    theme_array_num++;
    if (theme_array_num%theme_array.length == 0) {theme_array_num=0;}
    console.log(theme_array_num, theme_array.length);
    $ (":root").css("--background", theme_array[theme_array_num][0]);
    $ (":root").css("--front-primary", theme_array[theme_array_num][1]);
    $ (":root").css("--front-secondary", theme_array[theme_array_num][2]);

}