from app import app
from app.database import db
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from app.forms import LoginForm, RegistrationForm
from app.models import Account as User




