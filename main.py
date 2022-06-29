from flask import Flask, render_template, request
from main_class import Employees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, render_template

engine = create_engine('sqlite:///employees.db')
session = sessionmaker(bind=engine)
app = Flask(__name__)


@app.route('/')
def show_employees():
    with session.begin() as _session:
        data1 = [row for row in _session.query(Employees).all()]
        return render_template('show_employees.html', employees=data1)


@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    with session.begin() as _session:
        data1 = [row for row in _session.query(Employees).all()]
        if request.method == 'POST':
            name_inp = request.form.get('name')
            surname_inp = request.form.get('surname')
            birthday_inp = request.form.get('birthday')
            position_inp = request.form.get('position')
            salary_inp = request.form.get('salary')
            employee = Employees(name_inp, surname_inp, birthday_inp, position_inp, salary_inp)
            _session.add(employee)
        return render_template('add_employee.html', employees=data1)


@app.route('/edit_employee', methods=['GET', 'POST'])
def edit_employee():
    with session.begin() as _session:
        data1 = [row for row in _session.query(Employees).all()]
        if request.method == 'POST':
            id_to_edit = request.form.get('id')
            employee_to_be_edited = _session.query(Employees).get(id_to_edit)
            name_new = request.form.get('name')
            surname_new = request.form.get('surname')
            birthday_new = request.form.get('birthday')
            position_new = request.form.get('position')
            salary_new = request.form.get('salary')
            employee_to_be_edited.name = name_new
            employee_to_be_edited.surname = surname_new
            employee_to_be_edited.birthday = birthday_new
            employee_to_be_edited.position = position_new
            employee_to_be_edited.salary = salary_new
        return render_template('edit_employee.html', employees=data1)


@app.route('/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    with session.begin() as _session:
        data1 = [row for row in _session.query(Employees).all()]
        if request.method == 'POST':
            id_to_delete = request.form.get('id')
            employee_to_be_deleted = _session.query(Employees).get(id_to_delete)
            _session.delete(employee_to_be_deleted)
        return render_template('delete_employee.html', employees=data1)


if __name__ == '__main__':
    app.run()
