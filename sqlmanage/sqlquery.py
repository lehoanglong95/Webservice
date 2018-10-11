class SqlQuery:

    # def query_all(self):
    #     return 'SELECT province,district,ward FROM lba.cell_enodeb limit 100'


    def query_by(self, msisdn, part):
        print('SELECT * FROM Fb.phone_to_fb_part{} WHERE msisdn IN {}'.format(part, msisdn))
        return 'SELECT * FROM Fb.phone_to_fb_part{} WHERE msisdn IN {}'.format(part, msisdn)
