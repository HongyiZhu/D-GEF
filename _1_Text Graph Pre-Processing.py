import utils
import pickle
import sqlite3
from case_config import *

conn = sqlite3.connect('data.db')

cur = conn.cursor()

# TODO: Change the start/end date/year
for year in range(2012, 2020):
    for id in range(4):
        filename = "{}{}Q{}.txt".format(case, str(year), str(id + 1))
        preprocessedposts = open(filename, 'wb')

        month = ["03", "06", "09", "12"]
        day = ["31", "30", "30", "31"]

        # TODO: Change database schema
        # pull back the attachments within a given time period
        
        if case is 'webapp':
            sql = """
            select `id`, `published`, `title`, `description`
            from zero_day19 
            where attackType = 'webapps'
            and platform = 'php'
            and published BETWEEN '2012-01-01' AND '{}-{}-{}'
            order by `id`;
            """.format(str(year), month[id], day[id])
        if case is 'dos':
            sql = """
            select `id`, `published`, `title`, `description`
            from zero_day19 
            where attackType = 'dos'
            and platform = 'windows'
            and published BETWEEN '2012-01-01' AND '{}-{}-{}'
            order by `id`;
            """.format(str(year), month[id], day[id])
        cur.execute(sql)

        results = cur.fetchall()

        for row in results:
            postid = [row[0] for row in results]
            postdatetime = [row[1] for row in results]
            threadtitle = [row[2] for row in results]
            postcontent = [row[3] for row in results]

        store = []

        for i in range(len(postid)):
            # post = [postid[i], str(postdatetime[i]), utils.preprocessor(str(threadtitle[i] + postcontent[i]))]
            post = [postid[i], str(postdatetime[i]), utils.preprocessor(str(threadtitle[i]))]
            store.append(post)
            # string = "'{0}', '{1}', '{2}'".format(str(post[0]), str(post[1]), str(post[2]))
            # allopenscedges.write("%s\n" % string)

        pickle.dump(store,preprocessedposts)
        preprocessedposts.close()

# output pre-processed text into a notepad file (one record per line, comma seperated)