__author__ = 'c_disenc'


def create_file(file_name):
    fh = None

    try:
        fh = open(file_name, "r")

        #Reading upto 50 characters
        #print(fh.read(50))

        #Print whole files
        #print(fh.read())

        #Print readlines
        #print(fh.readline())
        #print(fh.readline())
        #print(fh.readline())


        #Returns character in a line
#        for val in fh.readline():
#            print("Returns Characters in a line ---- ", val)

        dict_db = {}

        #Returns Line
        for lines in fh.readlines():
            #print("Returns lines in character ---- ", val)
            string = "SEND: REGISTER"
            if string in lines:
                index_line = lines.index("SEND: REGISTER")
                if index_line in dict_db:
                    dict_db[lines[index_line+len(string):]] += 1
                else:
                    dict_db[lines[index_line+len(string):-1]] = 1

        print(dict_db)
                #print(lines)

        fh.close()

    except IOError as err:
            print(err)


create_file("telecan_logs")
