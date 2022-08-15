#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request


# In[2]:


app=Flask(__name__)


# In[3]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates=float(request.form.get("rates"))
        print(rates)
        model1=joblib.load("regression")
        r1=model.predict([[rates]])
        model1=joblib.load("Tree")
        r2=model.predict([[rates]])
        return(render_template("index.html",result1="r1",result2="r2"))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




