# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

from models import *

from django.utils import timezone

import views as v

d = v.dashboard

# Create your tests here.
class HttpMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the app index
    # and ensuring the response code is 200 (OK)
    def test_index_route_exists(self):
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)

    # Ensure get works
    def test_index_get(self):
        request = self.factory.get('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        request = self.factory.post('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_put(self):
        request = self.factory.put('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_delete(self):
        request = self.factory.delete('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_head(self):
        request = self.factory.head('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_options(self):
        request = self.factory.options('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_trace(self):
        request = self.factory.trace('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_patch(self):
        request = self.factory.patch('/')
        response = v.app_index(request)
        self.assertEqual(response.status_code, 200)

#Tests checking that that '/dashboard' properly handles HttpRequests
#Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class DashboardIndexHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_index_get(self):
        request = self.factory.get('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_post(self):
        request = self.factory.post('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_put(self):
        request = self.factory.put('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_delete(self):
        request = self.factory.delete('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_head(self):
        request = self.factory.head('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_options(self):
        request = self.factory.options('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_trace(self):
        request = self.factory.trace('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_patch(self):
        request = self.factory.patch('/dashboard')
        response = d.index(request)
        self.assertEqual(response.status_code, 405)

#Tests checking that that '/dashboard/home' properly handles HttpRequests
#Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardHomeHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_home_get(self):
        request = self.factory.get('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_home_post(self):
        request = self.factory.post('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_put(self):
        request = self.factory.put('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_delete(self):
        request = self.factory.delete('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_head(self):
        request = self.factory.head('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_options(self):
        request = self.factory.options('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_trace(self):
        request = self.factory.trace('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_patch(self):
        request = self.factory.patch('/dashboard/home')
        response = d.home(request)
        self.assertEqual(response.status_code, 405)

#Tests checking that that '/dashboard/change_graph' properly handles HttpRequests
#Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardChangeGraphHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_change_graph_get(self):
        request = self.factory.get('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_change_graph_post(self):
        request = self.factory.post('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_put(self):
        request = self.factory.put('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_delete(self):
        request = self.factory.delete('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_head(self):
        request = self.factory.head('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_options(self):
        request = self.factory.options('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_trace(self):
        request = self.factory.trace('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_patch(self):
        request = self.factory.patch('/dashboard/change_graph')
        response = d.change_graph(request)
        self.assertEqual(response.status_code, 405)

#Tests checking that that '/dashboard/doc' properly handles HttpRequests
#Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardDocHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_doc_get(self):
        request = self.factory.get('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_doc_post(self):
        request = self.factory.post('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_put(self):
        request = self.factory.put('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_delete(self):
        request = self.factory.delete('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_head(self):
        request = self.factory.head('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_options(self):
        request = self.factory.options('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_trace(self):
        request = self.factory.trace('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_patch(self):
        request = self.factory.patch('/dashboard/doc')
        response = d.doc(request)
        self.assertEqual(response.status_code, 405)

#Tests checking that that '/dashboard/new' properly handles HttpRequests
#Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardNewHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_new_get(self):
        request = self.factory.get('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_new_post(self):
        request = self.factory.post('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_put(self):
        request = self.factory.put('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_delete(self):
        request = self.factory.delete('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_head(self):
        request = self.factory.head('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_options(self):
        request = self.factory.options('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_trace(self):
        request = self.factory.trace('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_patch(self):
        request = self.factory.patch('/dashboard/new')
        response = d.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

#Tests checking that that '/dashboard/:id/edit' properly handles HttpRequests
#Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
#Tested on id #55
class DashboardEditHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_edit_get(self):
        request = self.factory.get('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_edit_post(self):
        request = self.factory.post('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_put(self):
        request = self.factory.put('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_delete(self):
        request = self.factory.delete('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_head(self):
        request = self.factory.head('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_options(self):
        request = self.factory.options('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_trace(self):
        request = self.factory.trace('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_patch(self):
        request = self.factory.patch('/dashboard/55/edit')
        response = d.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)


#Tests checking that that '/dashboard/:id' properly handles HttpRequests
#Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
#Tested on id #55
class DashboardIdHttpRequestMethodTests(TestCase):

    #setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_get(self):
        request = self.factory.get('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_post(self):
        request = self.factory.post('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_put(self):
        request = self.factory.put('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_delete(self):
        request = self.factory.delete('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_head(self):
        request = self.factory.head('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_options(self):
        request = self.factory.options('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_trace(self):
        request = self.factory.trace('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_patch(self):
        request = self.factory.patch('/dashboard/55')
        response = d.dashboard(request, 55)
        self.assertEqual(response.status_code, 200)


# Models Test
class ModelsTests(TestCase):
    def test_can_create_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())

        self.assertEquals(
            str(note),
            'Hey!',
        )
