import os
import json
from flask import Flask
from flask import request
import requests

app = Flask(__name__)


def hello_world():
    print('1111')
    print('2222')
    return 'Hello, Welcome to CloudBase!3\n'


# def add_job():
#     # args = request.args
#     print('------------')
#     args = request.data
#     if args is None:
#         print('None!')
#         return None
#     print(request.data)
#     args = args.decode('utf-8')
#     args = json.loads(args)
#     print('args: ', args)
#
#     jd = {
#         'title': args['payload']['title'],
#         'description': args['payload']['description'],
#         'requirement': args['payload']['requirement']
#     }
#     print(jd)
#
#     m = {
#         'data': {
#             'attributes': {
#                 'username': 'zhangzhongzheng',
#                 'password': 'zzz51270a'
#             }}
#     }
#     headers = {'Content-Type': 'application/vnd.api+json', 'Accept': 'application/vnd.api+json'}
#     # resp = requests.post(
#     #     'http://jobweekly-5gs1wdbdd6e26e01-1304983168.ap-shanghai.app.tcloudbase.com/api/login', data=json.dumps(m),
#     #     headers=headers)
#     # access_token = json.loads(resp.content)['data']['attributes']['access_token']
#     # print(access_token)
#
#     # headers = {'Content-Type': "application/json", 'Accept': 'application/json',
#     #            'Authorization': 'Bearer {}'.format(access_token)}
#     url = 'http://jobweekly-5gs1wdbdd6e26e01-1304983168.ap-shanghai.app.tcloudbase.com/api/threads'
#     title = '【{}内推】{}'.format(args['payload']['company'], args['payload']['title'])
#     content = '工作内容:\n{}\n\n工作要求:\n{}\n\n内推链接:{}'.format(args['payload']['description'], args['payload']['requirement'],
#                                                  args['payload']['link'])
#     m = {
#         'data': {
#             'type': 'threads',
#             'attributes': {
#                 'title': title,
#                 'content': content,
#                 'type': 1
#             },
#             'relationships': {
#                 'category': {
#                     'data': {
#                         'type': 'categories',
#                         'id': 1
#                     }
#                 }
#             }
#         }
#
#     }
#     # resp = requests.post(url, data=json.dumps(m), headers=headers)
#     # print(json.loads(resp.content))
#
#     # return 'args: {}'.format(json.loads(resp.content))
#     return 'args: {}'.format(json.dumps(jd))


app.add_url_rule('/', view_func=hello_world)
# app.add_url_rule('/job/add', view_func=add_job, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run(debug=True, host='0.0.0.0', port=5055)
