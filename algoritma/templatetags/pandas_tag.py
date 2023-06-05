from django import template

register = template.Library()

def get_data_head(df):
    html = ""
    for row in df.values:
        for value in row:
            dtsplit = value.split(' -> ')
            if len(dtsplit) > 1:
                html += f"<li>Jika membeli {dtsplit[0][2:-2]} maka akan juga membeli {dtsplit[1][2:-2]} dengan memiliki confidence atau tingkat kepercayaan sebesar {row[2]}.</li>"
    return html

def convert_data_frame_to_html_table_headers(df):
    html = "<tr>"
    for col in df.columns:
        html += f"<th scope='col' class='px-6 py-3'>{col}</th>"
    html += "</tr>"
    return html

def convert_data_frame_to_html_table_rows(df):
    html = ""
    for row in df.values:
        row_html = "<tr class='bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600'>"
        for value in row:
            row_html += f"<td class='px-6 py-4'>{value}</td>"
        row_html += "</tr>"
        html += row_html
    return html

register.filter("get_data_head", get_data_head)
register.filter("convert_data_frame_to_html_table_rows", convert_data_frame_to_html_table_rows)
register.filter("convert_data_frame_to_html_table_headers", convert_data_frame_to_html_table_headers)
