from datetime import time

from flask import Flask, render_template, request, jsonify, session

from DBConnection import Db

static_path="F:\\New folder\\homestead_fmg_systm\\static\\"

app = Flask(__name__)

app.secret_key="hiii"

@app.route('/admin_home')
def admin_home():
    return render_template('admin/home.html')

@app.route('/')
def landing_index():
    return render_template('landindex.html')

@app.route('/login_index')
def login_index():
    return render_template('loginindex.html')

@app.route('/admin_index')
def admin_index():
    return render_template('adminindex.html')




@app.route('/add_deliveryboy')
def add_deliveryboy():
    return render_template('admin/add delivery mgmt.html')

@app.route('/add_deliveryboy_post',methods=['post'])
def add_deliveryboy_post():
    name=request.form['textfield']
    place=request.form['textfield2']
    pin= request.form['textfield3']
    post= request.form['textfield4']
    image= request.files['filefield']
    image.save(static_path+'delivery_boy\\' + image.filename)
    path = "/static/delivery_boy/"+image.filename

    contact=request.form['textfield5']
    email= request.form['textfield6']
    d=Db()
    qry="insert into login""(username,password,type)values('"+email+"','"+contact+"','delivery_boy')"
    res=d.insert(qry)
    qry2="INSERT INTO `delivery_boy`(NAME,place,pin,post,image,email,contact,lid)VALUES('"+name+"','"+place+"','"+pin+"','"+post+"','"+path+"','"+email+"','"+contact+"','"+str(res)+"')"
    res = d.insert(qry2)
    return render_template('admin/add delivery mgmt.html')


@app.route('/edit_deliveryboy/<b>')
def edit_deliveryboy(b):
    c = Db()
    qry = "SELECT * FROM `delivery_boy` WHERE `delev_id`='" + b + "'"
    res = c.selectOne(qry)
    return render_template('admin/edit_delivery_boy.html',i=res)

@app.route('/edit_deliveryboy_post',methods=['post'])
def edit_deliveryboy_post():
    name=request.form['textfield']
    place=request.form['textfield2']
    pin= request.form['textfield3']
    post= request.form['textfield4']
    contact=request.form['textfield5']
    email= request.form['textfield6']
    delvid=request.form['delvid']
    c = Db()
    if 'filefield' in request.files:
        image = request.files['filefield']
        if image.filename != "":
            image.save(static_path + 'item\\' + image.filename)
            path = "/static/item/" + image.filename
            qry = "UPDATE `delivery_boy` SET `name`='"+name+"',`place`='"+place+"',`pin`='"+pin+"',`post`='"+post+"',`image`='"+path+"',`email`='"+email+"',`contact`='"+contact+"' WHERE `delev_id`='"+str(delvid)+"' "
            res = c.update(qry)
            return 'ok'
        else:
            qry = "UPDATE `delivery_boy` SET `name`='" + name + "',`place`='" + place + "',`pin`='" + pin + "',`post`='" + post + "',`email`='"+email+"',`contact`='"+contact+"' WHERE `delev_id`='"+str(delvid) + "' "
            res = c.update(qry)
            return 'ok'
    else:
        qry = "UPDATE `delivery_boy` SET `name`='"+name+"',`place`='"+place+"',`pin`='"+pin+"',`post`='"+post+"',`email`='"+email+"',`contact`='"+contact+"' WHERE `delev_id`='"+str(delvid)+"' "
        res = c.update(qry)
        return 'ok'
    return render_template('admin/edit_delivery_boy.html')






@app.route('/view_deliveryboy')
def view_deliveryboy():

    d=Db()
    res=d.select("SELECT * FROM delivery_boy")
    print(res)
    return render_template('admin/view delivery boy.html',data = res)


@app.route('/del_deliveryboy/<b>')
def del_deliveryboy(b):
    c = Db()
    qry = "DELETE FROM `delivery_boy` WHERE `delev_id`='" + b + "'"
    res = c.delete(qry)
    return view_deliveryboy()

@app.route('/view_deleveryboy_post',methods=['post'])
def view_deliveryboy_post():
    name = request.form['textfield']
    return 'ok'



@app.route('/add_pest')
def add_pest():
    return render_template('admin/add_pest.html')

@app.route('/add_pest_post',methods=['post'])
def add_pest_post():
    name=request.form['textfield']
    type=request.form['select']
    image= request.files['file']
    image.save(static_path + 'fert_pest\\' + image.filename)
    path = "/static/fert_pest/" + image.filename

    how_to_use = request.form['textarea']
    d=Db()
    qry="INSERT INTO `pesticide`(NAME,type,image,specification)VALUES('"+name+"','"+type+"','"+path+"','"+how_to_use+"')"
    res=d.insert(qry)
    return '''<script>alert('Added');window.location='/add_pest'</script>'''



@app.route('/view_pest')
def view_pest():
    d = Db()
    res = d.select("SELECT * FROM pesticide")
    print(res)
    return render_template('admin/view_pest.html',data=res)

@app.route('/delete_pest/<b>')
def delete_pest(b):
    d = Db()
    qry = "DELETE FROM `pesticide` WHERE `pid`='" + b + "'"
    res = d.delete(qry)
    print(res)
    return '''<script>alert('deleted');window.location='/view_pest'</script>'''

@app.route('/edit_pest/<b>')
def edit_pest(b):
    c = Db()
    qry = "SELECT * FROM `pesticide` WHERE `pid`='" + b + "'"
    res = c.selectOne(qry)
    return render_template('admin/edit_pest.html',i=res)


@app.route('/view_pest_post',methods=['post'])
def view_pest_post():
    pid = request.form['pid']
    name=request.form['textfield']
    type=request.form['textfield3']
    specification= request.form['textfield4']
    d = Db()
    if 'filefield' in request.files:
        image = request.files['filefield']
        if image.filename!="":
            image.save(static_path + 'fert_pest\\' + image.filename)
            path = "/static/fert_pest/" + image.filename
            qry = "UPDATE `pesticide` SET `name`='"+name+"',`image`='"+path+"',`type`='"+type+"',`specification`= '"+specification+"' WHERE `pid`='"+str(pid)+"'"
            res=d.update(qry)
            return '''<script>alert('Updated');window.location='/view_pest'</script>'''
        else:
            qry = "UPDATE `pesticide` SET `name`='" + name + "',`type`='" + type + "',`specification`= '" + specification + "' WHERE `pid`='" + str(pid) + "'"
            res = d.update(qry)
            return '''<script>alert('Updated');window.location='/view_pest'</script>'''
    else:
        qry = "UPDATE `pesticide` SET `name`='" + name + "',`type`='" + type + "',`specification`= '" + specification + "' WHERE `pid`='" + str(pid) + "'"
        res = d.update(qry)
        return '''<script>alert('Updated');window.location='/view_pest'</script>'''

@app.route('/view_fert')
def view_fert():
    d = Db()
    res = d.select("SELECT * FROM fertilizer")
    print(res)
    return render_template('admin/view_fert.html', data=res)

@app.route('/edit_fert_post', methods=['post'])
def edit_fert_post():
    fid = request.form['f_id']
    name = request.form['textfield']
    type = request.form['textfield3']
    specification = request.form['textarea']
    d = Db()
    if 'filefield' in request.files:
        image = request.files['filefield']
        if image.filename != "":
            image.save(static_path + 'fert_pest\\' + image.filename)
            path = "/static/fert_pest/" + image.filename
            qry = "UPDATE `fertilizer` SET `name`='" + name + "',`image`='" + path + "',`type`='" + type + "',`specification`= '" + specification + "' WHERE `fid`='" + str(
                fid) + "'"
            res = d.update(qry)
            return '''<script>alert('Updated');window.location='/view_fert'</script>'''
        else:
            qry = "UPDATE `fertilizer` SET `name`='" + name + "',`type`='" + type + "',`specification`= '" + specification + "' WHERE `fid`='" + str(
                fid) + "'"
            res = d.update(qry)
            return '''<script>alert('Updated');window.location='/view_fert'</script>'''
    else:
        qry = "UPDATE `fertilizer` SET `name`='" + name + "',`type`='" + type + "',`specification`= '" + specification + "' WHERE `fid`='" + str(
            fid) + "'"
        res = d.update(qry)
        return '''<script>alert('Updated');window.location='/view_fert'</script>'''


@app.route('/delete_fert/<b>')
def delete_fert(b):
    d = Db()
    qry = "DELETE FROM `fertilizer` WHERE `fid`='" + b + "'"
    res = d.delete(qry)
    print(res)
    return '''<script>alert('deleted');window.location='/view_fert'</script>'''

@app.route('/edit_fert/<b>')
def edit_fert(b):
    c = Db()
    qry = "SELECT * FROM `fertilizer` WHERE `fid`='" + b + "' "
    res = c.selectOne(qry)
    return render_template('admin/edit_fert.html', i=res)

@app.route('/add_fertile')
def add_fertile():
    return render_template('admin/add_fert.html')

@app.route('/add_fert_post', methods=['post'])
def add_fert_post():
    name = request.form['textfield']
    type = request.form['select']
    image = request.files['file']
    image.save(static_path + 'fert_pest\\' + image.filename)
    path = "/static/fert_pest/" + image.filename
    how_to_use = request.form['textarea']
    d = Db()
    qry = "INSERT INTO `fertilizer`(NAME,type,image,specification)VALUES('" + name + "','" + type + "','" + path + "','" + how_to_use + "')"
    res = d.insert(qry)
    return '''<script>alert('Added');window.location='/add_fertile'</script>'''



@app.route('/admn_reply')
def admn_reply():
    return render_template('admin/admn reply.html')

@app.route('/admn_reply_post',methods=['post'])
def admn_reply_post():
    reply=request.form['textarea']
    return 'ok'



@app.route('/sign_in')
def sign_in():
    return render_template('admin/sign in.html')

@app.route('/sign_in_post',methods=['post'])
def sign_in_post():
    username=request.form['u']
    password=request.form['p']
    c=Db()
    qry="SELECT * FROM `login` WHERE `username`='"+username+"' AND `password`='"+password+"'"
    res=c.selectOne(qry)
    if res is not None:
        session['lid']=res['login_id']
        type=res['type']
        if type=="admin":
            return admin_home()
        else:
            return '''<script>alert('Invalid Username or Password');window.location='/login_index'</script>'''
    else:
        return '''<script>alert('Invalid Username or Password');window.location='/login_index'</script>'''


@app.route('/view_complaint')
def view_complaint():
    c=Db()
    qry="SELECT `complaint`.* ,`user`.* FROM `user`,`complaint` WHERE `complaint`.`userInfo`= `user`.`lid`"
    res=c.select(qry)
    return render_template('admin/view complaint.html',data=res)

@app.route('/view_complaint_post')
def view_complaint_post():
    datefrom = request.form['datefrom']
    to = request.form['to']
    c=Db()
    qry="SELECT `complaint`.* ,`user`.* FROM `user`,`complaint` WHERE `complaint`.`userInfo`= `user`.`lid` and `complaint`.date between '"+datefrom+"' and '"+to+"'"
    res=c.select(qry)
    return render_template('admin/view complaint.html',data=res)

@app.route('/add_offers_post')
def add_offers_post():
    datefrom = request.form['datefrom']
    to = request.form['to']
    c=Db()
    qry="SELECT `complaint`.* ,`user`.* FROM `user`,`complaint` WHERE `complaint`.`userInfo`= `user`.`lid` and `complaint`.date between '"+datefrom+"' and '"+to+"'"
    res=c.select(qry)
    return render_template('admin/view complaint.html',data=res)



@app.route('/reply/<n>')
def reply(n):
    c=Db()
    qry="SELECT * FROM `complaint` WHERE `complaint_id`='"+n+"'"
    res=c.selectOne(qry)
    return render_template('admin/admn reply.html',res=res)


@app.route('/view_reply_post',methods=['post'])
def view_reply_post():
    reply = request.form['mm']
    cid=request.form['cid']
    # to = request.form['to']
    qry = "UPDATE `complaint` SET `reply`='"+reply+"',`status`='ok' WHERE `complaint_id`='"+str(cid)+"'"
    c=Db()
    res=c.update(qry)
    return '''<script>alert('replaied');window.location='/view_complaint'</script>'''





@app.route('/view_feedback')
def view_feedback():
    d = Db()
    res = d.select("SELECT * FROM feedback,user WHERE feedback.ulid=user.lid")
    print(res)

    return render_template('admin/view feedback.html',data= res)

@app.route('/view_feedback_post',methods=['post'])
def view_feedback_post():
    datefrom=request.form['textfield']
    to=request.form['textfield2']
    d=Db()
    qry="SELECT * FROM feedback,user WHERE feedback.ulid=user.lid and feedback.date between '"+datefrom+"' and '"+to+"' "
    res=d.select(qry)
    return render_template('admin/view feedback.html', data=res)




@app.route('/add_items')
def add_items():
    return render_template('admin/add_item.html')

@app.route('/add_items_post',methods=['post'])
def add_items_post():
    name = request.form['textfield']
    image=request.files['filefield']
    image.save(static_path+'item\\'+image.filename)
    path="/static/item/"+image.filename
    price = request.form['textfield2']
    description = request.form['textarea']

    d=Db()
    qry="INSERT INTO `items`(NAME,image,price,description)VALUES('"+name+"','"+path+"','"+price+"','"+description+"')"
    res=d.insert(qry)


    return 'ok'

# @app.route('/add_advertisements')
# def add_advertisements():
#     return render_template('admin/add_advertisement.html')
#
# @app.route('/add_advertisements_post',methods=['post'])
# def add_advertisements_post():
#
#     product_name = request.form['product_name']
#     product_image = request.files['product_image']
#
#     product_image.save(static_path + 'advertisement\\' + product_image.filename)
#     path = "/static/advertisement/" + product_image.filename
#
#     description = request.form['textarea']
#
#     d=Db()
#     q="INSERT INTO `advertisement`(`product_name`,`product_image`,`description`,`userid`)VALUES('"+product_name+"','"+path+"','"+description+"','"+str(session['lid'])+"')"
#     # qry="INSERT INTO `advertisement`(`product_name`,`product_image`,`description`,`userid`)VALUES('"+product_name+"','"+product_image+"','"+description+"','"+str(session['lid'])+"')"
#     res=d.insert(q)
#     return '''<script>alert('Added');window.location='/add_advertisements'</script>'''


@app.route('/view_advertisement')
def view_advertisement():
    d=Db()
    qry="SELECT `advertisement`.*,`user`.* FROM `advertisement` INNER JOIN `user` ON `advertisement`.`userid`=`user`.`lid`"
    res=d.select(qry)
    return render_template('admin/view_advertisement.html',data=res)

@app.route('/view_advertisement_post',methods=['post'])
def view_advertisement_post():
    adid=request.form['textfield']
    d=Db()
    qry="SELECT * FROM `advertisement` WHERE `adid`='"+adid+"'"
    res=d.select(qry)
    return render_template('admin/view_advertisement.html', data=res)


@app.route('/edit_advertisements/<b>')
def edit_advertisements(b):
    c=Db()
    qry="SELECT * FROM `advertisement` WHERE `adid`='"+b+"'"
    res=c.selectOne(qry)
    return render_template('admin/edit_advertisement.html',i=res)

@app.route('/edit_advertisements_post',methods=['post'])
def edit_advertisements_post():

    product_name = request.form['product_name']
    product_image = request.files['filefield']
    description = request.form['textarea']
    ad_id=request.form['ad_id']

    c=Db()
    if 'filefield'in request.files:
        image = request.files['filefield']
        if image.filename!="":
            image.save(static_path + 'advertisement\\' + image.filename)
            path = "/static/advertisement/" + image.filename
            qry="UPDATE `advertisement` SET `product_name`='"+product_name+"',`product_image`='"+path+"',`description`= '"+description+"'WHERE `adid`='"+str(ad_id)+"'"
            res=c.update(qry)
            return '''<script>alert('updated');window.location='/view_advertisement'</script>'''
        else:
            qry = "UPDATE `advertisement` SET `product_name`='" + product_name + "',`description`= '" + description + "'WHERE `adid`='" + str(ad_id) + "'"
            res = c.update(qry)
            return '''<script>alert('updated');window.location='/view_advertisement'</script>'''
    else:
        qry = "UPDATE `advertisement` SET `product_name`='" + product_name + "',`description`= '" + description + "'WHERE `adid`='" + str(ad_id) + "'"
        res = c.update(qry)
        return '''<script>alert('updated');window.location='/view_advertisement'</script>'''

@app.route('/del_advertisements/<b>')
def del_advertisements(b):
    c = Db()
    qry = "DELETE FROM `advertisement` WHERE `adid`='" + b + "'"
    res = c.delete(qry)
    return view_advertisement()



@app.route('/view_items')
def view_items():
    d=Db()
    qry="SELECT * FROM items"
    res=d.select(qry)

    return render_template('admin/view items.html',data=res)

@app.route('/view_items_post',methods=['post'])
def view_items_post():
    itemname=request.form['textfield']
    d=Db()
    qry="SELECT * FROM items where name like '%"+itemname+"%'"
    res=d.select(qry)
    return render_template('admin/view items.html', data=res)




@app.route('/view_user')
def view_user():
    d = Db()
    res = d.select("SELECT * FROM user")
    print(res)
    return render_template('admin/view_user.html', data=res)


@app.route('/view_user_post',methods=['post'])
def view_user_post():
    search=request.form['textfield']
    d = Db()
    qry="SELECT * FROM user where name like '%"+search+"%'"
    res=d.select(qry)


    return render_template('admin/view_user.html', data=res)



@app.route('/edit_items/<b>')
def edit_items(b):
    c=Db()
    qry="SELECT * FROM `items` WHERE `item_id`='"+b+"'"
    res=c.selectOne(qry)
    return render_template('admin/edit_item.html',i=res)

@app.route('/edit_items_post',methods=['post'])
def edit_items_post():
    name = request.form['textfield']
    itmid=request.form['itmid']
    price = request.form['textfield2']
    description = request.form['textarea']
    c=Db()
    if 'filefield'in request.files:
        image = request.files['filefield']
        if image.filename!="":
            image.save(static_path + 'item\\' + image.filename)
            path = "/static/item/" + image.filename
            qry="UPDATE `items` SET `name`='"+name+"',`image`='"+path+"',`price`='"+price+"',`description`= '"+description+"'WHERE `item_id`='"+str(itmid)+"'"
            res=c.update(qry)
            return '''<script>alert('updated');window.location='/view_items'</script>'''
        else:
            qry = "UPDATE `items` SET `name`='" + name + "',`price`='" + price + "',`description`= '" + description + "'WHERE `item_id`='" + str(itmid) + "'"
            res = c.update(qry)
            return '''<script>alert('updated');window.location='/view_items'</script>'''
    else:
        qry = "UPDATE `items` SET `name`='" + name + "',`price`='" + price + "',`description`= '" + description + "'WHERE `item_id`='" + str(itmid) + "'"
        res = c.update(qry)
        return '''<script>alert('updated');window.location='/view_items'</script>'''

@app.route('/del_items/<b>')
def del_items(b):
    c = Db()
    qry = "DELETE FROM `items` WHERE `item_id`='" + b + "'"
    res = c.delete(qry)
    return view_items()




@app.route('/view_regstrd_user')
def view_regstrd_user():
    return render_template('admin/view regstrd user.html')

@app.route('/view_regstrd_user_post', methods=['post'])
def view_regstrd_user_post():
    name= request.form['textfield']
    return 'ok'

@app.route('/view_review')
def view_review():
    d=Db()
    qry = "SELECT `review`.*,`items`.name AS iname,`user`.* FROM `user`,`items`,`review` WHERE `review`.`item_id`=`items`.`item_id` AND `review`.`ulid`=`user`.`lid` "
    res = d.select(qry)
    print("=====================",res)
    return render_template('admin/view review.html',data=res)



@app.route('/viewandapprove')
def viewandapprove():
    d=Db()
    qry = "select user.* from user,login  where  login.login_id=user.lid and login.type='pending'"
    res = d.select(qry)
    print("=====================",res)
    return render_template('admin/view_users.html',data=res)

@app.route('/view_review_post', methods=['post'])
def view_review_post():
    name= request.form['textfield']
    review = request.form['textarea']
    return 'ok'


@app.route('/view_rating')
def view_rating():
    d = Db()
    qry = "SELECT `rating`.*, `user`.`name`, `user`.`email` FROM `user` INNER JOIN `rating` ON `rating`.`ulid`=`user`.`lid`"
    res = d.select(qry)
    return render_template('admin/view rating.html',data=res)


@app.route('/admin_view_carss')
def admin_view_carss():
    db=Db()
    qry="SELECT `rating`.*, `user`.* FROM `user` INNER JOIN `rating` ON `rating`.`ulid`=`user`.`lid`"
    res=db.select(qry)
    ar_rt = []
    for im in range(0, len(res)):
        val = str(res[im]["rating"])
        ar_rt.append(val)
    fs = "/static/full.jpg"
    hs = "/static/half.jpg"
    es = "/static/empty.jpg"
    arr = []
    print(ar_rt)
    for rt in ar_rt:
            print(rt)
            a = float(rt)

            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]
                arr.append(ar)

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]
                arr.append(ar)

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]
                arr.append(ar)

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]
                arr.append(ar)

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]
                arr.append(ar)

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]
                arr.append(ar)

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]
                arr.append(ar)

            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]
                arr.append(ar)

            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]
                arr.append(ar)

            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]
                arr.append(ar)

            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
                arr.append(ar)
    print(arr)
    return render_template('admin/admin_view_rating.html',data=res,r1=arr,ln=len(arr))





#------------------------------------------------------------------andoid-------------------------------------------------------------------

@app.route('/addintowishlist',methods=['post'])
def addintowishlist():
    c = Db()
    uid = request.form['uid']
    itemid = request.form['pid']
    d = Db()
    qry = "INSERT INTO `wishlist`(ulid,`itemid`,`date`)VALUES('"+uid+"','"+itemid+"',curdate())"
    res = c.insert(qry)
    return  jsonify(status='ok')



@app.route('/bankcheack',methods=['post'])
def bankcheack():
    c = Db()
    print("888888888888888888888888888888888888888888888888888")
    accno = request.form['account_no']
    total=request.form['total']
    print("-------------------------------------------------------------------",total)
    pin=request.form['pin_no']
    p_id=request.form['p_id']
    lid=request.form['lid']
    d = Db()
    qry = "SELECT * FROM `bank` WHERE `accno`='"+accno+"' AND `pin`='"+pin+"'"
    res = c.selectOne(qry)
    mybal=res['balance']
    if int(mybal)>int(total):
        qryee = "INSERT INTO `payment`(`productid`,`amount`,`date`,ulid)VALUES('"+p_id+"','"+total+"',curdate(),'"+lid+"')"
        resee = c.insert(qryee)
        ww="UPDATE `bank` SET `balance`= `balance`-'"+total+"' WHERE `pin`='"+pin+"'"
        tt=d.update(ww)
        return  jsonify(status='ok')
    else:
        return  jsonify(status='no')



@app.route('/addintreview',methods=['post'])
def addintreview():
    c = Db()
    uid = request.form['lid']
    itemid = request.form['pid']
    fdk=request.form['feedback']
    d = Db()
    qry = "insert into review(item_id,ulid,review,date)values('"+itemid+"','"+uid+"','"+fdk+"',curdate())"
    res = c.insert(qry)
    return  jsonify(status='ok')


@app.route('/and_view_pesticide',methods=['post'])
def and_view_pesticide():
    c = Db()
    qry = "SELECT * FROM `pesticide`"
    res = c.select(qry)
    print(res)
    return  jsonify(status='ok',data=res)


@app.route('/and_view_wish',methods=['post'])
def and_view_wish():
    c = Db()
    lid=request.form['lid']
    qry = "SELECT `items`.*,product.* FROM `items`,`wishlist`,`user`,`product` WHERE `user`.`lid`=`wishlist`.`ulid`  AND `wishlist`.`itemid`=`product`.`product_id` AND  `product`.`item_id`=`items`.`item_id` AND `wishlist`.`ulid`='"+lid+"'"
    res = c.select(qry)
    print(qry)
    return  jsonify(status='ok',data=res)


@app.route('/and_add_pesticide',methods=['post'])
def and_add_pesticide():
    c = Db()
    name = request.form['textfield']
    pid=request.form['pid']
    image = request.form['image']
    type = request.forhomestead_fmg_systmm['type']
    specification = request.form['specification']
    d = Db()
    qry = "INSERT INTO `pesticide`(`pid`,`name`,`type`,`image`,`specification`)VALUES('"+pid+"','"+name+"','"+type+"','"+image+"','"+specification+"')"
    res = c.insert(qry)
    return  jsonify(status='ok')

@app.route('/and_add_offer',methods=['post'])
def and_add_offer():
    c = Db()
    name = request.form['description']
    pid=request.form['pid']

    d = Db()
    qry = "INSERT INTO `offers`(`product_id`,`date`,`description`)VALUES('"+pid+"',curdate(),'"+name+"')"
    res = c.insert(qry)
    return  jsonify(status='ok')

@app.route('/and_view_fertilizer',methods=['post'])
def and_view_fertilizer():
    c = Db()
    qry = "SELECT * FROM `fertilizer`"
    res = c.select(qry)
    print(res)
    return jsonify(status='ok', data=res)


@app.route('/and_add_fertilizer',methods=['post'])
def and_add_fertilizer():
    c = Db()
    fid = request.form['fid']

    name = request.form['textarea']
    type = request.form['type']
    image = request.form['image']
    specification = request.form['specification']
    d = Db()
    qry = "INSERT INTO `fertilizer`(`fid`,`name`,`type`,`image`,`specification`)VALUES('"+fid+"','"+name+"','"+type+"','"+image+"','"+specification+"')"
    res = c.insert(qry)
    return jsonify(status='ok')



@app.route('/and_add_offers',methods=['post'])
def and_add_offers():
    c = Db()
    product_id = request.form['product_id']
    date = request.form['date']
    description = request.form['description']
    d = Db()
    qry = "INSERT INTO `offers` (`product_id`,`offer_id`,`date`,`description`)VALUES('"+product_id+"','"+date+"','"+description+"')"
    res = c.insert(qry)
    return jsonify(status='ok')


@app.route('/and_view_offers_post',methods=['post'])
def and_view_offers():
    c = Db()
    product_id = request.form['prid']
    qry = " SELECT `items`.*,`offers`.* FROM `offers`,`items`,`product` WHERE `items`.`item_id`=`product`.`item_id` AND `product`.`product_id`=`offers`.`product_id` AND `product`.`product_id`" \
          "='"+product_id+"'"
    res = c.select(qry)
    print(qry)
    return jsonify(status='ok',data=res)



@app.route('/and_add_complaint_post',methods=['post'])
def and_add_complaint_post():
    c = Db()
    userInfo = request.form['uid']
    cp = request.form['cmp']


    d = Db()
    qry = "INSERT INTO `complaint`(`userInfo`,`complaint`,`reply`,`date`,`status`)VALUES('"+userInfo+"','"+cp+"','pending',curdate(),'pending')"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)




@app.route('/and_view_delevery_boy',methods=['post'])
def and_view_delevery_boy():
    c = Db()
    delev_id = request.form['delev_id']
    qry = "SELECT * FROM `delivery_boy`"
    res = c.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/prpost',methods=['post'])
def and_add_product_post():
    item_id = request.form['iid']
    user_id = request.form['lid']
    lati = request.form['lati']
    longi = request.form['longi']
    c = Db()
    qry = "INSERT INTO `product`(item_id,user_id,latin,longin)VALUES('" + item_id + "','" + user_id + "','"+lati+"','"+longi+"')"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)


@app.route('/item_load',methods=['post'])
def and_item_load_post2():
    c = Db()
    qry = "select * from items"
    res = c.select(qry)
    return jsonify(status='ok',data=res)



@app.route('/viewothers',methods=['post'])
def viewothers():
    c = Db()
    lid=request.form['lid']
    qry = "select * from user where lid!='"+lid+"'"
    res = c.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/viewitemmore',methods=['post'])
def and_view_item_more_post():
    c = Db()
    item_id = request.form['itd']
    qry = "SELECT * FROM `items` WHERE `item_id`= '"+item_id+"'"
    res = c.selectOne(qry)
    return jsonify(status='ok',name=res['name'],img=res['image'],price=res['price'],des=res['description'])


@app.route('/and_add_advertisement_post', methods=['post'])
def and_add_advertisement_post():
    product_name = request.form['product_name']
    description = request.form['description']
    img = request.form['img']
    lid = request.form['lid']
    import time, datetime
    from encodings.base64_codec import base64_decode
    import base64
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(img)
    fh = open("F:\\New folder\\homestead_fmg_systm\\static\\advertisement\\" + timestr + ".jpg", "wb")
    path = "/static/advertisement/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    d = Db()
    qry = "insert INTO `advertisement`(product_name,description,product_image,userid,date)VALUES('" + product_name + "','" + description + "','" + path + "','" + lid + "',curdate())"
    print(qry)
    res = d.insert(qry)
    return jsonify(status='ok')



@app.route('/and_things_post', methods=['post'])
def and_things_post():
    product_name = request.form['nn']
    description = request.form['dd']
    price=request.form['pp']
    img = request.form['ii']
    lid = request.form['lid']
    latiii=request.form['ll']
    loooo = request.form['oo']
    print("productname====",product_name)
    print("description====", description)
    print("price====", price)

    import time, datetime
    from encodings.base64_codec import base64_decode
    import base64
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(img)
    fh = open("F:\\New folder\\homestead_fmg_systm\\static\\item\\" + timestr + ".jpg", "wb")
    path = "/static/item/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    d = Db()
    qry="INSERT INTO `items`(NAME,image,price,description)VALUES('"+product_name+"','"+path+"','"+price+"','"+description+"')"
    print(qry)
    res = d.insert(qry)
    qry22 = "INSERT INTO `product`(item_id,user_id,latin,longin)VALUES('" + str(res) + "','" + lid + "','"+latiii+"','"+loooo+"')"
    res22=d.insert(qry22)
    return jsonify(status='ok')






@app.route('/and_login_post',methods=['post'])
def and_login_post():
    username = request.form['username']
    password = request.form['password']
    c = Db()
    qry = "SELECT * FROM `login` WHERE `username`='" + username + "' AND `password`='" + password + "'"
    res = c.selectOne(qry)
    if res is not None:
        type = res['type']
        if type == "user":
            return jsonify(status='ok',lid=res['login_id'],type=res['type'])
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')


@app.route('/and_sign_up_post',methods=['post'])
def and_sign_up_post():
    c = Db()
    gender = request.form['gen']
    print("-------------------------------------------555555555555555555555555555",gender)
    name = request.form['name']
    place = request.form['place']
    pin = request.form['pin']
    post = request.form['post']
    district = request.form['district']
    phone = request.form['phone']
    email = request.form['email']
    img=request.form['img']
    import datetime
    import base64
    import random
    x = random.randint(000, 999)
    a = base64.b64decode(img)
    fh = open("F:\\New folder\\homestead_fmg_systm\\static\\userpic\\"+str(x) + ".jpg", "wb")
    path = "/static/userpic/" +str(x)  + ".jpg"
    fh.write(a)
    fh.close()
    d = Db()
    qry2 = "INSERT INTO `login`(username,password,type)VALUES('" + email + "','" + phone + "','pending')"
    res2 = c.insert(qry2)
    qry = "INSERT INTO `user`(NAME,image,gender,place,pin,post,district,phone,email,lid)VALUES('"+name+"','"+path+"','"+gender+"','"+place+"','"+pin+"','"+post+"','"+district+"','"+phone+"','"+email+"','"+str(res2)+"')"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)

@app.route('/and_add_review_post')
def and_add_review_post():
    description = request.form['textarea']
    c = Db()
    qry = "INSERT INTO `and_add_review_post`(description)VALUES('" + description + "'"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)

@app.route('/apporrjt/<n>')
def apporrjt(n):
    c = Db()
    qry = "UPDATE `login` SET TYPE='user' WHERE `login_id`='"+n+"'"
    res = c.update(qry)
    return viewandapprove()

@app.route('/apporrjt2/<n>')
def apporrjt2(n):
    c = Db()
    qry = "UPDATE `login` SET TYPE='reject' WHERE `login_id`='"+n+"'"
    res = c.update(qry)
    return viewandapprove()


# @app.route('/and_send_feedback_post',methods=['post'])
# def and_send_feedback_post():
#     uid = request.form['uid']
#     feedback = request.form['dd']
#     c = Db()
#     qry = "INSERT INTO `feedback`(DEFAULT id,feedback,date)VALUES('" + uid + "' , '" + feedback + "', curdate())"
#     res = c.insert(qry)
#     return jsonify(status='ok')


# @app.route('/and_add_item_post')
# def and_add_item_post():
#     description = request.form['textarea']
#     c = Db()
#     qry = "INSERT INTO `and_add_item_post`(description)VALUES('" + description + "'"
#     res = c.insert(qry)

@app.route('/and_add_offers_post',methods=['post'])
def and_add_offers_post():
    description = request.form['textarea']
    c = Db()
    qry = "INSERT INTO `and_add_offers_post`(description)VALUES('" + description + "'"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)

@app.route('/and_add_rating_post',methods=['post'])
def and_add_rating_post():
    rat = request.form['rr']
    lid=request.form['lid']
    c = Db()
    qry = "INSERT INTO `rating`(ulid,rating,date)VALUES('" + lid + "','"+rat+"',curdate())"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)






@app.route('/and_view_advertisement_post',methods=['post'])
def and_view_advertisement_post():
    c = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM `advertisement` WHERE `userid`='"+lid+"'"
    res = c.select(qry)
    return jsonify(status='ok', data=res)



@app.route('/and_view_advertisement_postss2',methods=['post'])
def and_view_advertisement_postss2():
    c = Db()
    lid=request.form['lid']
    qry = "SELECT `user`.*,`advertisement`.* FROM `advertisement`,`user` WHERE `user`.lid=`advertisement`.`userid` AND `advertisement`.`userid`!='"+lid+"'"
    res = c.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/and_view_item_post',methods=['post'])
def and_view_item_post():
    c = Db()
    lid=request.form['lid']
    qry = "SELECT `items`.*,product.* FROM `items`,`product`,`user` WHERE `user`.`lid`=`product`.`user_id` AND `product`.`item_id`=`items`.`item_id` AND product.item_id=items.item_id and `product`.`user_id`!='"+lid+"'"
    res = c.select(qry)
    return jsonify(status='ok', data=res)



@app.route('/and_view_item_postttt',methods=['post'])
def and_view_item_postttt():
    c = Db()
    lid=request.form['lid']
    qry = " SELECT `items`.*,product.* FROM `items`,`product`,`user` WHERE `user`.`lid`=`product`.`user_id` AND `product`.`item_id`=`items`.`item_id` AND product.item_id=items.item_id and `product`.`user_id`='"+lid+"'"
    res = c.select(qry)
    print(qry)
    return jsonify(status='ok', users=res)

@app.route('/and_view_notification_post',methods=['post'])
def and_view_notification_post():
    n_id = request.form['n_id']
    c = Db()
    qry = "SELECT * FROM `notification`"
    res = c.insert(qry)
    return jsonify(status='ok', data=res)

@app.route('/and_view_offers',methods=['post'])
def and_view_offers_post():
    product_id= request.form['product_id']
    c = Db()
    qry = "SELECT `items`.*,`offers`.* FROM `offers`,`items`,`product` WHERE `items`.`item_id`=`product`.`item_id` AND `product`.`product_id`=`offers`.`offer_id` AND `product`.`product_id`='"+product_id+"'"
    res = c.select(qry)
    return jsonify(status='ok',data=res)



@app.route('/and_view_purchase_history_post',methods=['post'])
def and_view_purchase_history_post():
    lid = request.form['lid']
    c = Db()
    qry = "SELECT `items`.*,payment.* FROM `items`,`user`,`payment`,product WHERE `payment`.`productid`=`product`.`product_id` AND `product`.`item_id`=`items`.`item_id` AND `payment`.`ulid`='"+lid+"'"
    print(qry)
    res = c.select(qry)
    return jsonify(status='ok', data=res)


@app.route('/and_view_reply_post',methods=['post'])
def and_view_reply_post():
    lid = request.form['lid']
    c=Db()
    qry="select * from complaint where userInfo='"+str(lid)+"'"
    res=c.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/and_view_review_post',methods=['post'])
def and_view_review_post():
    c = Db()
    qry = "SELECT `review`.*,`user`.name AS username,`items`.name AS item_name FROM `items`,`user`,`review` WHERE `review`.`item_id`=`items`.`item_id` AND `review`.`ulid`=`user`.`lid` "
    res = c.select(qry)
    return jsonify(status='ok',data=res)


@app.route('/and_view_rating_post',methods=['post'])
def and_view_rating_post():
    c = Db()
    qry = "SELECT `user`.*,`rating`.* FROM `rating`,`user` WHERE `user`.`lid`=`rating`.`ulid`"
    res = c.select(qry)
    return jsonify(status='ok',data=res)


@app.route('/deluserproduct',methods=['post'])
def deluserproduct():
    c = Db()
    itd=request.form['itd']
    qry = "DELETE FROM `product` WHERE `product_id`='" + itd + "'"
    res = c.delete(qry)
    print(qry)
    return jsonify(status='ok')

@app.route('/remove_adv',methods=['post'])
def remove_adv():
    c = Db()
    itd=request.form['advid']
    qry = "DELETE FROM `advertisement` WHERE `adid`='" + itd + "'"
    res = c.delete(qry)
    return jsonify(status='ok')

@app.route('/deluserproduct2',methods=['post'])
def deluserproduct2():
    c = Db()
    itd=request.form['itd']
    qry = "DELETE FROM `wishlist` WHERE `list_id`='" + itd + "'"
    res = c.delete(qry)
    return jsonify(status='ok')


@app.route('/and_newpassword', methods=["post"])
def new_password():
    password = request.form["password"]
    lid = request.form["lid"]
    c = Db()

    qry = "UPDATE`login`SET`password`='" + password + "'WHERE login_id='" + lid + "'"
    print(qry)
    res = c.update(qry)
    return jsonify(status='ok')


@app.route('/in_message2', methods=['POST'])
def message():
    fr_id = request.form["fid"]
    to_id = request.form["toid"]
    message = request.form["msg"]
    query7 = "insert into chat(sender_id,receiver_id,chat_msg,date,time) values ('" + fr_id + "' ,'" + to_id + "','" + message + "',curdate(),curtime())"

    print(query7);
    c=Db()
    cc=c.insert(query7)
    return jsonify(status='ok')



@app.route('/view_message2', methods=['POST'])
def msg():
    fid = request.form["fid"]
    toid = request.form["toid"]
    lmid = request.form['lastmsgid'];
    query="select sender_id as sender_id,chat_msg as chat_msg,date,chatid from chat where chatid>'"+lmid+"' AND ((receiver_id='"+toid+"' and  sender_id='"+fid+"') or (receiver_id='"+fid+"' and sender_id='"+toid+"')  )  order by chatid asc"
    c = Db()






    cc = c.select(query)
    print(cc)
    return jsonify(status='ok',res1=cc)


@app.route('/view_message2', methods=['POST'])
def msgg():
    fid = request.form["fid"]
    toid = request.form["toid"]
    lmid = request.form['lastmsgid'];
    query="select sender_id as sender_id,chat_msg as chat_msg,date,chatid from chat where chatid>'"+lmid+"' AND ((receiver_id='"+toid+"' and  sender_id='"+fid+"') or (receiver_id='"+fid+"' and sender_id='"+toid+"')  )  order by chatid asc"
    c = Db()
    cc = c.select(query)
    print(cc)
    return jsonify(status='ok',res1=cc)




@app.route('/mynotifi',methods=['post'])
def mynotifi():
    c = Db()
    print("hoi")
    latitude=request.form['ll']
    print("ok")
    longitude=request.form['oo']
    rr="SELECT * FROM `product` WHERE `latin`='"+latitude+"'  AND `longin`='"+longitude+"'"
    u=Db()
    e=u.select(rr)
    if len(e)>0:
        for i in e:
            if i['latin']>=2000:
                print("yessssss")
                return jsonify(status='ok')
            else:
                print("nooooo")
                return jsonify(status='no')
    else:
        return jsonify(status='no')





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
