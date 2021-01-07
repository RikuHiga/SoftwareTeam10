class LectureDBManagement:
    def refarence(self,i):     #引数に指定された箇所の情報を返す
        try:     #fileが存在しなかったら空のfile作成
            with open("lecture_db.csv",'x') as f:
                pass
        except FileExistsError:
            pass
        with open("lecture_db.csv") as f:
            read_info = f.readlines()[i]
        return read_info

    def search(self,status,Lecture,kind,credit,time,grade):     #検索にヒットしたもののindex番号を返す
        true_count = 0
        compare = []
        result = []
        search_list = [status,Lecture,kind,credit,time,grade]
        with open("lecture_db.csv") as f:
            lines = f.readlines()
            line_list = [line.strip().split(",") for line in lines]

            for i in range(len(line_list)):
                for j in range(len(search_list)):
                    if search_list[j] != "" and search_list[j] != "-1":
                        compare.append(search_list[j])
                        if line_list[i][j] == search_list[j]:
                            true_count += 1
                if len(compare) == true_count:
                    result.append(i)
                true_count = 0
                compare.clear()
        return result
    
    def update(self,flag,status,Lecture,kind,credit,time,grade,description):     #講義情報を追加・更新する
            if flag >= 0:
                insert_Data = status+","+Lecture+","+kind+","+credit+","+time+","+grade+","+description+"\n"
                with open("lecture_db.csv") as f:
                    lines = f.readlines()
                    lines[flag] = insert_Data
                with open("lecture_db.csv","w") as f:
                    f.writelines(lines)
            elif flag  == -1:
                update_Info = "\n"+status+","+Lecture+","+kind+","+credit+","+time+","+grade+","+description
                with open("lecture_db.csv","a") as f:
                    f.write(update_Info)
                    
                    
    def delete(self,place):     #講義情報を削除する
            with open("lecture_db.csv")as f:
                lines = f.readlines()
                lines.pop(place)
            with open("lecture_db.csv","w") as f:
                f.writelines(lines)
