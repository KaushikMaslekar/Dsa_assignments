#include <iostream>
#include <string>

using namespace std;

struct Student {
    int rollNumber;
    string name;
    string division;
    string address;
};

struct Node {
    Student data;
    Node* left;
    Node* right;
};

class StudentBST {
private:
    Node* root;

    Node* insert(Node* node, Student data) {
        if (node == nullptr) {
            return new Node{data, nullptr, nullptr};
        }

        if (data.rollNumber < node->data.rollNumber) {
            node->left = insert(node->left, data);
        } else if (data.rollNumber > node->data.rollNumber) {
            node->right = insert(node->right, data);
        }
        return node;
    }

    void inorder(Node* node) {
        if (!node) return;
        inorder(node->left);
        cout << "Roll No: " << node->data.rollNumber << ", Name: " << node->data.name
            << ", Division: " << node->data.division << ", Address: " << node->data.address << endl;
        inorder(node->right);
    }

    Node* search(Node* node, int rollNo) {
        if (node == nullptr || node->data.rollNumber == rollNo) {
            return node;
        }
        if (rollNo < node->data.rollNumber) {
            return search(node->left, rollNo);
        } 
        return search(node->right, rollNo);
    }

    Node* findMin(Node* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }

    Node* deleteNode(Node* node, int rollNo) {
        if (node == nullptr) return nullptr;

        if (rollNo < node->data.rollNumber) {
            node->left = deleteNode(node->left, rollNo);
        } else if (rollNo > node->data.rollNumber) {
            node->right = deleteNode(node->right, rollNo);
        } else {
            if (node->left == nullptr) {
                Node* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                Node* temp = node->left;
                delete node;
                return temp;
            } else {
                Node* temp = findMin(node->right);
                node->data = temp->data;
                node->right = deleteNode(node->right, temp->data.rollNumber);
            }
        }
        return node;
    }

public:
    StudentBST() {
        root = nullptr;
    }

    void insert(Student data) {
        root = insert(root, data);
    }

    void display() {
        if (root == nullptr) {
            cout << "No Student records found." << endl;
        } else {
            inorder(root);
        }
    }

    void search(int rollNumber) {
        Node* result = search(root, rollNumber);
        if (result) {
            cout << "Student Found!" << endl;
            cout << "Roll No: " << result->data.rollNumber << ", Name: " << result->data.name
                << ", Division: " << result->data.division << ", Address: " << result->data.address << endl;
        } else {
            cout << "Student record not found." << endl;
        }
    }

    void deleteStudent(int rollNumber) {
        root = deleteNode(root, rollNumber);
    }
};

int main() {
    StudentBST tree;

    int choice, roll;
    Student temp;
    do {
        cout << "\nStudent Information System\n";
        cout << "1. Add Student\n2. Delete Student\n3. Search Student\n4. Display All Students\n5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter Roll No: ";
                cin >> temp.rollNumber;
                cin.ignore();
                cout << "Enter Name: ";
                getline(cin, temp.name);
                cout << "Enter Division: ";
                getline(cin, temp.division);
                cout << "Enter Address: ";
                getline(cin, temp.address);
                tree.insert(temp);
                break;
            case 2:
                cout << "Enter Roll No to delete: ";
                cin >> roll;
                tree.deleteStudent(roll);
                break;
            case 3:
                cout << "Enter Roll No to search: ";
                cin >> roll;
                tree.search(roll);
                break;
            case 4:
                tree.display();
                break;
            case 5:
                cout << "Exiting program...\n";
                break;
            default:
                cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 5);

    return 0;
}
