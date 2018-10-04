from flask import jsonify,json
import re
import psycopg2
from main.db import Database


db_content=Database()

class CustomerOrders:
    def make_order(self, customer_id, order_date, payment, current_location, my_items=list()):
        """ performs the logic for addding an order to a list"""
        customer_order = []
        order_items = my_items
        try:
            sql="INSERT INTO orders(user_id,date,payment_mode,order_items,location) VALUES(%s,%s,%s,%s,%s)"
            db_content.cur.execute(sql,(customer_id, order_date, payment, json.dumps(order_items),current_location))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)}),400       
        return jsonify({'message':'order succussfully made '}),201

    def get_all_orders(self):
        db_content.dict_cursor.execute("SELECT orders.date,orders.payment_mode, orders.order_items,users.username,users.phone_number from orders INNER JOIN users ON orders.user_id=users.user_id ")
        data=db_content.dict_cursor.fetchall() 
        return jsonify({'results':data})                                                       

    def create_account(self,username,phone,email,password):
        if not username or password or phone or email:
            return jsonify({'error':'some fields are missing'}),400
        if not username.isalpha() or len(username) < 4 or username.strip() == "":
            return jsonify({'error':'wrong username format'}), 403

        if not phone.isdigit() or phone.strip() == "" or len(phone) < 10 or len(phone) > 12:
            return jsonify({'error': 'wrong phone number format'}), 403
        email_match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if email_match == None:
	        return jsonify({'error':'Incorrect email format'})
        try:
            sql="INSERT INTO users(username,phone_number,email,password) VALUES(%s,%s,%s,%s)"
            db_content.cur.execute(sql,(username,phone,email,password))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)})        
        return jsonify({'message':'succussfully registered'}),201
        
    def get_role(user_id):
        db_content.cur.execute("SELECT user_type users WHERE user_id='{}'".format(user_id))
        role=db_content.cur.fetchone()
        for rol in role:
            return role[0]

    def get_menu_items(self):
        db_content.dict_cursor.execute("SELECT * FROM Items")
        data=db_content.dict_cursor.fetchall()
        return jsonify({'results':data}),200

    def add_menu_items(self,item_name,price,quantity):
        try:
            sql="INSERT INTO Items(item_name,price,quantity) VALUES(%s,%s,%s)"
            db_content.cur.execute(sql,(item_name,price,quantity))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)})        
        return jsonify({'message':'Item is added'}),201

    def get_history_orders(self,user_id):
        db_content.dict_cursor.execute("SELECT * from orders WHERE user_id='{}'".format(user_id))
        data=db_content.dict_cursor.fetchall()
        return jsonify({'user_order':data}),200
    
    def get_specific_order(self,orderid):
        db_content.dict_cursor.execute("SELECT * from orders WHERE order_id='{}'".format(orderid))
        data=db_content.dict_cursor.fetchall()
        return jsonify({'user_order':data}),200
    
    def update_status(self,status,orderid):
        sql="UPDATE orders SET status='"+status+"' WHERE order_id='{}'".format(orderid)
        db_content.cur.execute(sql)
        return jsonify({'message':'order succussfully updated'}),201


    def make_admin(self,user_id):
        adm='admin'
        sql="UPDATE users SET user_type='"+adm+"' WHERE user_id='{}'".format(user_id)
        db_content.cur.execute(sql)
        return jsonify({'message':'changed to admin succussfully'}),201
