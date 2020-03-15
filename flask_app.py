# Code Deployed in Remote Server
from flask import Flask, request
from efficient_apriori import apriori
import io
import csv

app = Flask(__name__)

def aprioriFun(f,ms,mc):
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    transactions = []
    for row in csv_input:
        #print(row)
        s = set(row)
        if('' in s):
            s.remove('')
        transactions.append(tuple(s))
    itemsets, rules = apriori(transactions, min_support=ms, min_confidence=mc)
    ans = ''
    for _ in rules:
        ans+=(str(str(_) + "\n"))
    return ans



@app.errorhandler(404)
def page_not_found(e):
    return ("Refer Readme for URL format", 404)


@app.route("/upload/<ms>/<mc>", methods=['POST'])
def upload_file(ms,mc):
    try:
        if request.method == 'POST':
            f = request.files['file']
            try:
                if(float(ms)>=0 and float(ms)<=1.0 and float(mc)>=0 and float(mc)>=0):
                    ms = float(ms)
                    mc = float(mc)
                else:
                    mc = 0.6
                    ms = 0.3
            except ValueError:
                mc = 0.6
                ms = 0.3
            except:
                raise Exception()
            finally:
                return (aprioriFun(f,ms,mc))
    except:
        return ("Refer Readme for URL format", 404)


if __name__ == "__main__":
    app.run(port=4996)