from app import app, forms, email
from app.battle import Battle
from randomaccesstoken import generate_access_token
from flask import render_template, flash, redirect, session, url_for, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from random import randint

queue = []
battles = []


def check_name(name):
    for i in set(name.lower()):
        if 96 < ord(i) < 123 or i == '_' or i == '-' or i == '.' or 47 < ord(i) < 58:
            continue
        else:
            return False
    return True


# @app.route('/api/<int:id_battle>', methods=['GET', 'POST'])
# def battle_api():
#     if request.method == 'POST':
#         pass
#     return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/battle', methods=['GET', 'POST'])
def battle():
    global battles
    if session.get('username', None) is None:
        return redirect('/')
    form = forms.SetShip()
    message = ""
    if len([request.args.items]) != 0 and request.method == 'GET' and session.get('setbattle') != 11:
        session['setbattle'] = 1
        if len(battles) == 0:
            battles.append([Battle(session.get('username'), session.get('battle_username'))])
            return render_template('battle.html', user=session.get("username"), id=session.get('battle_username'),
                                   battle=True, form=form, message="Set 4 point ship")
        elif session.get('username') in battles[session.get('id_battle')][0].ids():
            return render_template('battle.html', user=session.get("username"), id=session.get('battle_username'),
                                   battle=True, form=form, message="Set 4 point ship")
    if session.get('setbattle') == 11 and len(battles[session.get('id_battle')]) == 2 and session.get('wait', False):
        return render_template("battle.html", user=session.get('username'),
                               id=session.get('battle_username'), battle=True, wait=True)
    elif session.get('setbattle') == 11 and len(battles[session.get('id_battle')]) == 3:
        session['wait'] = None
        return render_template('sea_battle.html', user=session.get("username"), id=session.get('battle_username'),
                               battle=True, message="Battle")
    if form.validate_on_submit():
        print(session.get('setbattle'), session.get('id_pers'), session.get('id_battle'),
              battles[session.get('id_battle')][0].decript(form.c.data, f=True), int(form.d.data), battles)
        if session.get('setbattle') == 1:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 4, 2)
                if f:
                    session['setbattle'] = 2
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 3 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set 4 point ship")
            else:
                x = battles[session.get('id_battle')][0].decript(form.c.data, f=True)
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'), x, int(form.d.data), 4, 1)
                if f:
                    session['setbattle'] = 2
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 3 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set 4 point ship")
        elif session.get('setbattle') == 2:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 3, 2)
                if f:
                    session['setbattle'] = 3
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 3 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 3 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 3, 1)
                if f:
                    session['setbattle'] = 3
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 3 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 3 point ship")
        elif session.get('setbattle') == 3:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 3, 2)
                if f:
                    session['setbattle'] = 4
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 3 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 3, 1)
                if f:
                    session['setbattle'] = 4
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 3 point ship")
        elif session.get('setbattle') == 4:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 2)
                if f:
                    session['setbattle'] = 5
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 2 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 1)
                if f:
                    session['setbattle'] = 5
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 2 point ship")
        elif session.get('setbattle') == 5:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 2)
                if f:
                    session['setbattle'] = 6
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 2 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 1)
                if f:
                    session['setbattle'] = 6
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 2 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 2 point ship")
        elif session.get('setbattle') == 6:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 2)
                if f:
                    session['setbattle'] = 7
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 2 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 2, 1)
                if f:
                    session['setbattle'] = 7
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 2 point ship")
        elif session.get('setbattle') == 7:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 2)
                if f:
                    session['setbattle'] = 8
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 1 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 1)
                if f:
                    session['setbattle'] = 8
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set first 1 point ship")
        elif session.get('setbattle') == 8:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 2)
                if f:
                    session['setbattle'] = 9
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 1 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 1)
                if f:
                    session['setbattle'] = 9
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set second 1 point ship")
        elif session.get('setbattle') == 9:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 2)
                if f:
                    session['setbattle'] = 10
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set fourth 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 1 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 1)
                if f:
                    session['setbattle'] = 10
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set fourth 1 point ship")
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set third 1 point ship")
        elif session.get('setbattle') == 10:
            if form.p.data == 'Vertically':
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 2)
                if f:
                    session['setbattle'] = 11
                    if len(battles[session.get('id_battle')]) == 1:
                        battles[session.get('id_battle')].append(True)
                        session['wait'] = True
                    elif len(battles[session.get('id_battle')]) == 2:
                        return redirect("sea_battle")
                    return render_template("battle.html", user=session.get('username'),
                                           id=session.get('battle_username'), wait=True)
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set fourth 1 point ship")
            else:
                f = battles[session.get('id_battle')][0].setup(session.get('id_pers'),
                                                               battles[session.get('id_battle')][0].decript(form.c.data,
                                                                                                            f=True),
                                                               int(form.d.data), 1, 1)
                if f:
                    session['setbattle'] = 11
                    if len(battles[session.get('id_battle')]) == 1:
                        battles[session.get('id_battle')].append(True)
                        session['wait'] = True
                    elif len(battles[session.get('id_battle')]) == 2:
                        return redirect("sea_battle")
                    return render_template("battle.html", user=session.get('username'),
                                           id=session.get('battle_username'), wait=True)
                else:
                    flash('Incredible')
                    return render_template('battle.html', user=session.get("username"), form=form,
                                           id=session.get('battle_username'),
                                           battle=True, message="Set fourth 1 point ship")
        else:
            return render_template("battle.html", user=session.get('username'),
                                   id=session.get('battle_username'), wait=True)
    else:
        return render_template("battle.html", user=session.get('username'),
                    id=session.get('battle_username'), wait=True)


@app.route('/start_battle')
def start_battle():
    if session.get('username', None) is not None:
        if len(queue) != 0:
            if session.get('username') not in queue[-1] and not session.get('battle', False):
                i = queue[-1]
                if len(i) == 1:
                    queue[-1] = (i[0], session.get('username'))
                    session['battle'] = True
                    session['id_battle'] = len(queue) - 1
                    session['id_pers'] = 2
                    session['battle_username'] = queue[-1][0]
                    return redirect(
                        url_for("battle", id=session.get('id_battle'), user=session.get('username'), battle=True))
                else:
                    queue.append((session.get('username'),))
                    session['battle'] = True
                    session['id_battle'] = len(queue) - 1
                    session['id_pers'] = 1
                    return render_template('start_battle.html', user=session.get('username'), battle=True)
            else:
                if len(queue[-1]) == 1 and session.get('username') not in queue[-1]:
                    i = queue[-1]
                    queue[-1] = (i[0], session.get('username'))
                    session['battle'] = True
                    session['id_battle'] = len(queue) - 1
                    session['id_pers'] = 2
                    session['battle_username'] = queue[-1][0]
                    return redirect(
                        url_for("battle", id=session.get('id_battle'), user=session.get('username'), battle=True))
                elif len(queue[-1]) == 2 and session.get('username') in queue[-1]:
                    return redirect(
                        url_for("battle", id=session.get('id_battle'), user=session.get('username'), battle=True))
                else:
                    return render_template('start_battle.html', user=session.get('username'), battle=True)
        else:
            queue.append((session.get('username'),))
            session['battle'] = True
            session['id_battle'] = 0
            session['id_pers'] = 1
            if len(queue[session.get('id_battle')]) != 1:
                return redirect(url_for("battle", id=session.get('id_battle'), battle=True))
            return render_template('start_battle.html', user=session.get('username'), battle=True)
    else:
        return redirect(url_for("index", user=session.get('username')))


@app.route('/sea_battle', methods=['GET', 'POST'])
def sea_battle():
    form = forms.SetHit()
    if session.get('id_pers') == 1:
        if battles[session.get('id_battle')][0].win() == 3:
            if form.validate_on_submit():
                if battles[session.get('id_battle')][0].turn() == 1:
                    s = str(form.c.data) + str(form.d.data)
                    battles[session.get('id_battle')][0].hit(battles[session.get('id_battle')][0].decript(s))
                else:
                    flash("This is not your turn")
            m1, m2 = battles[session.get('id_battle')][0].map(1)
            s1, s2 = "", ""
            for i in m1:
                for j in i:
                    s1 += str(j)
                s1 += "\n"
            s1 = s1[:-2]
            for i in m2:
                for j in i:
                    s2 += str(j)
                s2 += "\n"
            s2 = s2[:-2]
            return render_template('sea_battle.html', title='Battle', form=form, user=session.get('username'), m1=s1,
                                   m2=s2)
        elif battles[session.get('id_battle')][0].win() == 1:
            session['setbattle'] = None
            session['battle'] = False
            session['id_battle'] = None
            session['id_pers'] = None
            session['battle_username'] = None
            return render_template('win', id=session.get('username'))
        else:
            session['setbattle'] = None
            session['battle'] = False
            session['id_battle'] = None
            session['id_pers'] = None
            session['battle_username'] = None
            return render_template('win', id=session.get('battle_username'))
    elif session.get('id_pers') == 2:
        if battles[session.get('id_battle')][0].win() == 3:
            if form.validate_on_submit():
                if battles[session.get('id_battle')][0].turn() == 2:
                    s = str(form.c.data) + str(form.d.data)
                    battles[session.get('id_battle')][0].hit(battles[session.get('id_battle')][0].decript(s))
                else:
                    flash("This is not your turn")
            s1, s2 = "", ""
            for i in m1:
                for j in i:
                    s1 += j
                s1 += "\n"
            s1 = s1[:-2]
            for i in m2:
                for j in i:
                    s2 += j
                s2 += "\n"
            s2 = s2[:-2]
            return render_template('sea_battle.html', title='Battle', form=form, user=session.get('username'), m1=s1,
                                   m2=s2)
        elif battles[session.get('id_battle')][0].win() == 2:
            session['setbattle'] = None
            session['battle'] = False
            session['id_battle'] = None
            session['id_pers'] = None
            session['battle_username'] = None
            return render_template('win', id=session.get('username'))
        else:
            session['setbattle'] = None
            session['battle'] = False
            session['id_battle'] = None
            session['id_pers'] = None
            session['battle_username'] = None
            return render_template('win', id=session.get('battle_username'))
    else:
        return redirect(url_for("index.html",
                                title='Home',
                                user=session.get('username', 'Guest'),
                                battles=session.get('battles'),
                                wins=session.get('wins')))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if session.get('username', None) is not None:
        return redirect('/')
    form = forms.RegForm()
    if form.validate_on_submit():
        token = generate_access_token.random_access_token()
        if not check_name(form.username.data):
            flash("Only Latin characters and digits can be in the username, as well as '_', '-', '.'")
            return render_template('registration.html', title='Registration',
                                   form=form,
                                   user=session.get('username', 'Guest'))
        if len(form.password.data) < 8:
            flash("Password length is not enough")
            return render_template('registration.html', title='Registration',
                                   form=form,
                                   user=session.get('username', 'Guest'))
        if form.password.data != form.repassword.data:
            flash("Password mismatch")
            return render_template('registration.html', title='Registration',
                                   form=form,
                                   user=session.get('username', 'Guest'))
        for i in db.fetch():
            if form.username.data.lower() == i[1]:
                flash(form.username.data.lower() + " is not available")
                return render_template('registration.html', title='Registration',
                                       form=form,
                                       user=session.get('username', 'Guest'))
            elif form.email.data == i[2]:
                flash(form.email.data.lower() + " have account")
                return render_template('registration.html', title='Registration',
                                       form=form,
                                       user=session.get('username', 'Guest'))
            elif token == i[5]:
                token = generate_access_token.random_access_token()
        email.send_email_reg(form.email.data, form.username.data, form.password.data)
        db.insert(form.username.data.lower(), form.email.data, generate_password_hash(form.password.data), token)
        session['username'] = form.username.data
        session['token'] = token
        session['email'] = form.email.data
        session['battles'] = 0
        session['wins'] = 0
        flash(form.username.data.lower() + " is registered")
        return redirect('/')
    return render_template('registration.html', title='Registration',
                           form=form,
                           user=session.get('username', 'Guest'))


@app.route("/delete_account")
def delete_account():
    if session.get('username', None) is not None:
        db.delete(session.get('username'))
    email.send_email_del(session.get("email"), session.get("username"))
    session.pop('username', None)
    session.pop('battles', None)
    session.pop('email', None)
    session.pop('wins', None)
    session.pop('token', None)
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    session['setbattle'] = None
    session['battle'] = False
    session['id_battle'] = None
    session['id_pers'] = None
    session['battle_username'] = None
    return render_template("index.html",
                           title='Home',
                           user=session.get('username', 'Guest'),
                           battles=session.get('battles'),
                           wins=session.get('wins'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('battles', None)
    session.pop('wins', None)
    session.pop('token', None)
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username', None) is not None:
        return redirect(url_for('index'))
    elif session.get('token', None) is not None:
        for i in db.fetch():
            if session.get('token') == i[5]:
                session['username'] = i[1]
                session['email'] = i[2]
                session['battles'], session['wins'] = i[4], i[5]
                session['token'] = i[5]
                flash('Access granted for ' + i[1])
                return redirect(url_for('index'))
        session.pop('token', None)
        return redirect(url_for('login'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        # session['remember_me'] = form.remember_me.data
        for i in db.fetch():
            if (form.username.data.lower() == i[1] or form.username.data.lower() == i[2]) and check_password_hash(i[3],
                                                                                                                  form.password.data):
                session['username'] = i[1]
                session['battles'], session['wins'] = i[4], i[5]
                session['token'] = i[5]
                session['email'] = i[2]
                flash('Access granted for ' + i[1])
                return redirect(url_for('index'))
            elif (form.username.data.lower() == i[1] or form.username.data.lower() == i[2]) and not check_password_hash(
                    i[3], form.password.data):
                flash('Access denied')
                return redirect(url_for('login'))
        flash('Account with username "' + form.username.data + '" does not exist')
        return redirect(url_for('login'))
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           user=session.get('username', 'Guest'))
