from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/First')
def First():
    return render_template('First.html')

@FAI.route('/Context')
def Context():
    return render_template('Context.html',name='Achyuth',age=23)

if __name__=='__main__':
    FAI.run(debug=True)