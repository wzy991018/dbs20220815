{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "439f7259",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "03bbb9b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "afb6c84b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__call__',\n",
       " '__class__',\n",
       " '__delattr__',\n",
       " '__dict__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__le__',\n",
       " '__lt__',\n",
       " '__module__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " '__weakref__',\n",
       " '_find_error_handler',\n",
       " '_get_exc_class_and_code',\n",
       " '_register_error_handler',\n",
       " 'add_template_filter',\n",
       " 'add_template_global',\n",
       " 'add_template_test',\n",
       " 'add_url_rule',\n",
       " 'after_request',\n",
       " 'app_context',\n",
       " 'app_ctx_globals_class',\n",
       " 'auto_find_instance_path',\n",
       " 'before_first_request',\n",
       " 'before_request',\n",
       " 'config_class',\n",
       " 'context_processor',\n",
       " 'create_global_jinja_loader',\n",
       " 'create_jinja_environment',\n",
       " 'create_url_adapter',\n",
       " 'debug',\n",
       " 'default_config',\n",
       " 'dispatch_request',\n",
       " 'do_teardown_appcontext',\n",
       " 'do_teardown_request',\n",
       " 'endpoint',\n",
       " 'env',\n",
       " 'errorhandler',\n",
       " 'finalize_request',\n",
       " 'full_dispatch_request',\n",
       " 'get_send_file_max_age',\n",
       " 'got_first_request',\n",
       " 'handle_exception',\n",
       " 'handle_http_exception',\n",
       " 'handle_url_build_error',\n",
       " 'handle_user_exception',\n",
       " 'has_static_folder',\n",
       " 'import_name',\n",
       " 'inject_url_defaults',\n",
       " 'iter_blueprints',\n",
       " 'jinja_env',\n",
       " 'jinja_environment',\n",
       " 'jinja_loader',\n",
       " 'jinja_options',\n",
       " 'json_decoder',\n",
       " 'json_encoder',\n",
       " 'log_exception',\n",
       " 'logger',\n",
       " 'make_config',\n",
       " 'make_default_options_response',\n",
       " 'make_null_session',\n",
       " 'make_response',\n",
       " 'make_shell_context',\n",
       " 'name',\n",
       " 'open_instance_resource',\n",
       " 'open_resource',\n",
       " 'open_session',\n",
       " 'permanent_session_lifetime',\n",
       " 'preprocess_request',\n",
       " 'preserve_context_on_exception',\n",
       " 'process_response',\n",
       " 'propagate_exceptions',\n",
       " 'raise_routing_exception',\n",
       " 'register_blueprint',\n",
       " 'register_error_handler',\n",
       " 'request_class',\n",
       " 'request_context',\n",
       " 'response_class',\n",
       " 'root_path',\n",
       " 'route',\n",
       " 'run',\n",
       " 'save_session',\n",
       " 'secret_key',\n",
       " 'select_jinja_autoescape',\n",
       " 'send_file_max_age_default',\n",
       " 'send_static_file',\n",
       " 'session_cookie_name',\n",
       " 'session_interface',\n",
       " 'shell_context_processor',\n",
       " 'should_ignore_error',\n",
       " 'static_folder',\n",
       " 'static_url_path',\n",
       " 'teardown_appcontext',\n",
       " 'teardown_request',\n",
       " 'template_filter',\n",
       " 'template_folder',\n",
       " 'template_global',\n",
       " 'template_test',\n",
       " 'templates_auto_reload',\n",
       " 'test_cli_runner',\n",
       " 'test_cli_runner_class',\n",
       " 'test_client',\n",
       " 'test_client_class',\n",
       " 'test_request_context',\n",
       " 'testing',\n",
       " 'trap_http_exception',\n",
       " 'try_trigger_before_first_request_functions',\n",
       " 'update_template_context',\n",
       " 'url_defaults',\n",
       " 'url_map_class',\n",
       " 'url_rule_class',\n",
       " 'url_value_preprocessor',\n",
       " 'use_x_sendfile',\n",
       " 'wsgi_app']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(Flask)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b27d63f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1= joblib.load(\"LR_DBS\")\n",
    "        r1=model1.predict([[rates]])\n",
    "        model2=joblib.load(\"Tree\")\n",
    "        r2=model2.predict([[rates]])                         \n",
    "        return(render_template(\"index.html\",result1=r1,result2=r2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "121f3c06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:19] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:19] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Pc\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:24] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    app.run(port=8000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77ea0924",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
