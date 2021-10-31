import re
identifiers = '[_a-zA-Z][_a-zA-Z0-9]*'
integers = '[0-9][0-9]*'
float_val = '\d+\.\d*'
float_val1 = '\.\d+'
octal = '\\[0-9]{1,3}'
hexadecimal = '\\x[0-9a-fA-F]{1,2}'
sp_operations = {'=':'assign_op', '+':'add_op', '-':'sub_op', '*':'mul_op', '/':'div_op', '%':'mod_op', '\'':'single_quotes', '"':'double_quotes', '(':'left_paranthesis',')':'right_paranthesis'}
keywords = ['auto','const','double','float','int','short','struct','unsigned','break','continue','else','for','long','signed','switch','void','case','default','enum','goto','register','sizeof','typedef','volatile','char','do','extern','if','return','static','union','while']
delimiter = ';'
#sp - special characters
parsed_array = []
with open('raw_data.txt','r') as file:
    while True:
        new_char = file.read(1)
        if new_char=="":
            break
        token = new_char
        identifier = re.fullmatch(identifiers, new_char)
        if identifier:
            val='IDENTIFIER'
        integer = re.fullmatch(integers, new_char)
        floats = re.fullmatch(float_val, new_char)
        if integer:
            val='INTEGER'
        if new_char == ".":
            while new_char!='':
                next_char = file.read(1)
                if next_char == "":
                    break
                if next_char == " ":
                    break
                temp_char = token + next_char
                float_dot = re.fullmatch(float_val1, temp_char)
                if float_dot:
                    token = temp_char
                    val = "FLOAT" 
                else:
                    break   
        if new_char != '' and new_char in sp_operations.keys():
            val = sp_operations[new_char]
            parsed_array.append((new_char,val))

        while new_char!='' and identifier: 
            next_char = file.read(1)
            if next_char == "":
                break
            if next_char == " ":
                break
            temp_char = token + next_char
            identifier = re.fullmatch(identifiers, temp_char)
            if identifier:
                token = temp_char
                val="IDENTIFIER"
        while new_char!='' and integer or floats:
            next_char = file.read(1)
            if next_char == "":
                break
            if next_char == " ":
                break
            temp_char = token + next_char
            integer = re.fullmatch(integers, temp_char)
            floats = re.fullmatch(float_val, temp_char)
            if floats:
                token = temp_char
                val = "FLOAT"
            elif integer:
                token = temp_char
                val="INTEGER"
        if val == 'IDENTIFIER' or val == 'INTEGER' or val=='FLOAT':
          parsed_array.append((token,val))
        token=''
        val=""
        if new_char=="":
            break 

valueToBeRemoved= (' ','')

parsed_array = [value for value in parsed_array if value != valueToBeRemoved]

valueToBeRemoved= ('\n','')

parsed_array = [value for value in parsed_array if value != valueToBeRemoved]

for i in parsed_array:
    print(i)
    