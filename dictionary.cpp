#include <iostream>
using namespace std;

struct Node{
    string key, value;
    Node* left;
    Node* right;

    Node(string k, string v){
        key = k;
        value = v;
        left = right = nullptr;
    }
};

class Dictionary{
    private:
        Node* root;
        
        Node* insert(Node* node, string key, string value){
            if (!node) return new Node(key, value);

            if(key < node->key)
                node->left = insert(node->left, key, value);
            else if(key > node -> key)
                node->right = insert(node->right, key, value);
            else{
                node-> value = value;
            }
            return node;
        }

        Node* search(Node* node, string key){
            if (!node || node->key == key) return node;

            if (key < node->key){
                return search(node->left, key);
            }
            return search(node->right, key);
        }

        Node* deleteNode(Node* node, string key){
            if (!node) return node;

            if (key < node->key){
                node->left = deleteNode(node->left, key);
            }
            else if (key > node->key){
                node->right = deleteNode(node->right, key);
            }
            else{
                if (!node->left){
                    Node* temp = node->right;
                    delete node;
                    return temp;
                }
                else if (!node->right){
                    Node* temp = node->left;
                    delete node;
                    return temp;
                }

                Node* temp = minValueNode(node->right);
                node->key = temp->key;
                node->value = temp->value;
                node->right = deleteNode(node->right, temp->key);
            }
            return node;

        }

        Node* minValueNode(Node* node){
            Node* current = node;
            while (current && current -> left){
                current = current -> left;
            }            
            return current;    
        }

        void inorder(Node* node){
            if(!node) return;

            inorder(node->left);
            cout<<node->key << " :" << node-> value<< endl;
            inorder (node->right);
        }

    public:
        Dictionary(){
            root = nullptr;}

        void insert(string key, string value){
            root = insert(root, key, value);
        }

        void search(string key){

            Node* result = search(root, key);
            if(result){
                cout << "Key: " << key << ", Value: " << result->value << endl;
            }
            else{
                cout << "Key not found" << endl;
            }
        }

        void remove(string key){
            root = deleteNode(root, key);
        }

        void display(){
            inorder(root);
        }
};

int main(){
    Dictionary dict;
    int choice;
    string key, value;

    do{
        cout << "\nDictionary Operations:";
        cout << "\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit";
        cout << "\nEnter choice: ";
        cin >> choice;

        switch (choice){
            case 1:
                cout << "Enter the key: ";
                cin >> key;
                cout << "Enter the value: ";
                cin >> value;
                dict.insert(key, value);
                break;

            case 2:
                cout << "Enter the key to search: ";
                cin >> key;
                dict.search(key);
                break;

            case 3:
                cout << "Enter the key to delete: ";
                cin >> key;
                dict.remove(key);
                break;

            case 4:
                dict.display();
                break;
                
                
        }
    }while (choice != 5);

    return 0;
}