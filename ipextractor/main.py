from ip_extract.client import ExctractClient
from cfn_logs.client import CFNLogsClient
from flask import Flask,render_template
import jinja2



class CFNtoLocation:

    app = Flask(__name__)
    

    @app.route('/')
    def publish_logs():
        # with open("templates/json.list") as filehandle:
        #     ip_list = list(filehandle.read())
            return render_template('output.list')

    def run():

        extract_client = ExctractClient()
        cfn_client = CFNLogsClient()

        
        cfn_client.main()
        extract_client.parser()


def main():
    CFNtoLocation.run()
    CFNtoLocation.app.run(host='0.0.0.0', port=2727, debug=True)



if __name__ == '__main__':
    main()