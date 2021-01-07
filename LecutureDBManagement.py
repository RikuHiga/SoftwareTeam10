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