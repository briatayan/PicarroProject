import requests
import json
import unittest
import threading

class TestCLIServiceMethods(unittest.TestCase):

### BEGIN TESTING METHODS ###

    def test_add_valid_task(self):
        url = 'http://localhost:5000/'
        validData = {"task" : "This is from the unit test"}
        res = requests.post(url + 'add-task', json=validData)
        res = json.loads(res.text)
        self.assertTrue(isinstance(res, int))

    def test_add_invalid_task_1(self):
        url = 'http://localhost:5000/'
        invalidData = {"task" : ""}
        res = requests.post(url + 'add-task', json=invalidData)
        res = json.loads(res.text)
        self.assertEqual(res.get("success"), False)

    def test_add_invalid_task_2(self):
        url = 'http://localhost:5000/'
        invalidData = {"task" : 0}
        res = requests.post(url + 'add-task', json=invalidData)
        res = json.loads(res.text)
        self.assertEqual(res.get("success"), False)

    def test_add_invalid_task_3(self):
        url = 'http://localhost:5000/'
        invalidData = { "tas" : "this is invalid" }
        res = requests.post(url + 'add-task', json=invalidData)
        res = json.loads(res.text)
        self.assertEqual(res.get("success"), False)

    def test_get_valid_task(self):
        url = 'http://localhost:5000/'
        res = requests.get(url + 'get-task/1')
        self.assertNotEqual(res.status_code, 404)

    def test_get_invalid_task(self):
        url = 'http://localhost:5000/'
        res = requests.get(url + 'get-task/500')
        self.assertEqual(res.status_code, 404)

    def test_get_all_tasks(self):
        url = 'http://localhost:5000/'
        res = requests.get(url + 'get-all-tasks')
        self.assertTrue(res is not None)

    def test_change_valid_task_desc(self):
        url = 'http://localhost:5000/'
        data = { "task" : "this is testing the description update" }
        res = requests.put(url + 'change-task-description/1', json=data)
        self.assertEqual(res.status_code, 200)

    def test_change_invalid_task_desc_1(self):
        url = 'http://localhost:5000/'
        data = { "task" : None }
        res = requests.put(url + 'change-task-description/1', json=data)
        self.assertEqual(res.status_code, 400)

    def test_change_invalid_task_desc_2(self):
        url = 'http://localhost:5000/'
        data = {"task" : "this is testing the invalid description update"}
        res = requests.put(url + 'change-task-description/500', json=data)
        self.assertEqual(res.status_code, 404)

    def test_change_invalid_task_desc_3(self):
        url = 'http://localhost:5000/'
        data = { "tas" : "this is invalid" }
        res = requests.put(url + 'change-task-description/1', json=data)
        self.assertEqual(res.status_code, 400)

    def test_valid_complete_task(self):
        url = 'http://localhost:5000/'
        res = requests.put(url + 'complete-task/1')
        self.assertEqual(res.status_code, 200)

    def test_invalid_complete_task(self):
        url = 'http://localhost:5000/'
        res = requests.put(url + 'complete-task/500')
        self.assertEqual(res.status_code, 404)

    def test_valid_incomplete_task(self):
        url = 'http://localhost:5000/'
        validData = {"task" : "This is to test the incomplete task function"}
        resAdd = requests.post(url + 'add-task', json=validData)
        resAdd = json.loads(resAdd.text)
        requests.put(url + 'complete-task/' + str(resAdd))
        res = requests.put(url + 'incomplete-task/'+ str(resAdd))
        self.assertEqual(res.status_code, 200)

    def test_invalid_incomplete_task(self):
        url = 'http://localhost:5000/'
        res = requests.put(url + 'incomplete-task/500')
        self.assertEqual(res.status_code, 404)

    def test_valid_delete_task(self):
        url = 'http://localhost:5000/'
        res = requests.delete(url + 'delete-task/1')
        self.assertEqual(res.status_code, 200)

    def test_invalid_delete_task(self):
        url = 'http://localhost:5000/'
        res = requests.delete(url + 'delete-task/500')
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()
