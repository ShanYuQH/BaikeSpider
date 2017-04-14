# -*- coding:utf-8 -*-


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<head><title>百度百科抓取词条</title></head>")
        fout.write("<body>")
        fout.write('<table style="table-layout:fixed;" border ="1" width=100%>')
        fout.write("<tr>")
        fout.write('<th align="left">URL</th>')
        fout.write('<th align="left">Title</th>')
        fout.write("<th>Summary</th>")
        fout.write("</tr>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write('<td style="WORD-WRAP: break-word" width="35%%">%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td style="WORD-WRAP: break-word" width="55%%">%s</td>' % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
