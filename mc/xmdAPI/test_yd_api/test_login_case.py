#登录case
# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from xmdAPI.config import config

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpLogin


class TestLoginCase(Base):

    def test_Login_wrongName(self):
        """测试登录接口,异常登录（错误的用户名，正确的密码）,@author:liusai"""
        result = helpLogin('liuliuliu', "uat.portal")
        self.assertEqual(result['message'], "CRM登陆失败,用户名不存在")

    def test_Login_wrongPwd(self):
        """测试登录接口,异常登录（正确的用户名，错误的密码）,@author:liusai"""
        result = helpLogin('wb4005', "uat")
        self.assertEqual(result['message'], "CRM登陆失败,用户名或密码不正确")


    def test_Login_empty(self):
        """测试登录接口,异常登录（空用户名，空密码）,@author:liusai"""
        result = helpLogin("", "")
        self.assertEqual(result['message'], "CRM登陆失败")


    def test_Login_emptyUsername(self):
        """测试登录接口,异常登录（空用户名，正确密码）,@author:liusai"""
        result = helpLogin("", "uat.portal")
        self.assertEqual(result['message'], "CRM登陆失败")

    def test_login_success(self):
        """测试登录接口,登录成功,@author:liusai"""
        result = helpLogin("wb3005", "uat.portal")
        self.assertEqual(result['ok'],True)

    def test_Login_emptyPwd(self):
        """测试登录接口,异常登录（正确用户名，空密码）,@author:liusai"""
        result = helpLogin("wb3005", "")
        self.assertEqual(result['message'], "CRM登陆失败")


    def test_Login_blankspaceUsername(self):
        """测试登录接口,异常登录（正确用户名，错误密码（带空格））,@author:liusai"""
        result = helpLogin("wb3005", "uat.portal ")
        self.assertEqual(result['message'], "CRM登陆失败,用户名或密码不正确")

    def test_get_token(self):
        """测试登录接口,获得token,@author:liusai"""
        result = helpLogin("wb3005", "uat.portal")
        print(result)

