#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    cout<< "--------------------------"<<endl;
    cout<< "1 --- Creating a vector;"<<endl;
    cout<< "2 --- Inverting the elements of a vector;"<<endl;
    cout<< "3 --- Add an element to the end of a vector;"<<endl;
    cout<< "4 --- Remove the last element from the vector;"<<endl;
    cout<< "5 --- Change the content;"<<endl;
    cout<< "6 --- Insert in vector;"<<endl;
    cout<< "7 --- Delete an element from the vector;"<<endl;
    cout<< "8 --- Delete the vector;"<<endl;
    cout<< "9 --- I check if I have elements in the vector;"<<endl;
    cout<< "10--- I check how many elements the vector has;"<<endl;
    cout<< "0 --- Exit;"<<endl;
    cout<< "--------------------------"<<endl;
    vector<int>myVector;
    vector<int>::iterator it;
    int i,n;
    cin>>n;
    while(n)
    {
        if(n==1)
       {
        int dim, elem;
        cout<<"Choose the size of the vector: ";
        cin>>dim;
        cout<<"Enter vector elements: ";
        for(i=0;i<dim;i++)
        {
          cin>>elem;
          myVector.push_back(elem);
        }
        cout<<endl;
        cout << "This is our vector: ";
        for(it=myVector.begin();it!=myVector.end();it++)
                   cout<<*it<<" ";
        cout <<endl;
      }
      else
          if(n==2)
          {
            if(myVector.empty())
               cout<<"There are no elements in the vector. First create a vector! ";
            else
               {
                 reverse(myVector.begin(),myVector.end());
                 cout<<"Vector after inversion: "<<endl;
                 for(it=myVector.begin();it!=myVector.end();it++)
                            cout<<*it<<" ";
                 cout <<endl;
               }

          }
          else
              if(n==3)
              {
                int nr;
                if(myVector.empty())
                      cout<<"There are no elements in the vector. First create a vector! ";
               else
                {
                  cout<<"The item you are adding:";
                  cin>>nr;
                  myVector.push_back(nr);
                  cout<<"Vector after addition: "<<endl;
                  for(it=myVector.begin();it!=myVector.end();it++)
                            cout<<*it<<" ";
                  cout <<endl;
                }
              }
              else
                 if(n==4)
                 {
                   if(myVector.empty())
                         cout<<"There are no elements in the vector. First create a vector! "<<endl;
                   else
                   {
                     myVector.pop_back();
                  cout<<"Vector after removing the last element: "<<endl;
                  for(it=myVector.begin();it!=myVector.end();it++)
                            cout<<*it<<" ";
                  cout <<endl;
                   }
                 }
                 else
                    if(n==5)
                    {
                      if(myVector.empty())
                            cout<<"There are no elements in the vector. First create a vector! ";
                      else
                      {
                        vector<int>Vector;
                        vector<int>::iterator ite;
                        cout<<"Second vector: "<<endl;
                        int dimen, element;
                        cout<<"Choose the size of the vector: ";
                        cin>>dimen;
                        cout<<"Enter vector elements: ";
                        for(i=0;i<dimen;i++)
                        {
                            cin>>element;
                            Vector.push_back(element);
                        }
                        cout<<endl;
                        cout << "This is our second vector: ";
                        for(ite=Vector.begin();ite!=Vector.end();ite++)
                                 cout<<*ite<<" ";
                        cout <<endl;
                        cout <<endl;

                        cout << "This is our first vector: ";
                        for(it=myVector.begin();it!=myVector.end();it++)
                                 cout<<*it<<" ";
                        cout <<endl;
                        cout <<endl;

                        Vector.swap(myVector);
                        cout<<"After changing the content:"<<endl;
                        cout <<endl;
                        cout << "This is our first vector: ";
                        for(it=myVector.begin();it!=myVector.end();it++)
                                 cout<<*it<<" ";
                        cout <<endl;
                        cout <<endl;
                        cout << "This is our second vector: ";
                        for(ite=Vector.begin();ite!=Vector.end();ite++)
                                 cout<<*ite<<" ";
                        cout <<endl;
                        cout <<endl;
                        Vector.clear();
                      }
                    }
                    else
                        if(n==6)
                        {
                          if(myVector.empty())
                                cout<<"There are no elements in the vector. First create a vector! ";
                          else
                          {
                            cout<<"Create a vector:"<<endl;
                            vector<int>anothervector;
                            vector<int>::iterator y;
                            int di, el;
                        cout<<"Choose the size of the vector: ";
                        cin>>di;
                        cout<<"Enter vector elements: ";
                        for(i=0;i<di;i++)
                        {
                            cin>>el;
                            anothervector.push_back(el);
                        }
                        cout<<endl;
                        cout<<"This is our second vector: ";
                        for(y=anothervector.begin();y!=anothervector.end();y++)
                                 cout<<*y<<" ";
                        cout <<endl;
                        cout<<"Choose from which position to insert: ";
                        int m;
                        cin>>m;
                        y=myVector.begin();
                        myVector.insert(y+m,anothervector.begin(),anothervector.end());
                        cout<<"Our vector by insert: ";
                        for(it=myVector.begin();it!=myVector.end();it++)
                                   cout<<*it<<" ";
                        cout <<endl;
                        anothervector.clear();
                          }
                        }
                        else
                        {
                          if(n==7)
                          {
                            if(myVector.empty())
                                cout<<"There are no elements in the vector. First create a vector! ";
                            else
                            {
                              cout<<"Choose which item to delete: "<<endl;
                              cout<<"position =";
                              int pozitie;
                              cin>>pozitie;
                              myVector.erase(myVector.begin()+pozitie);
                              cout <<endl;
                              cout<<"New vector after deletion: ";
                              for(it=myVector.begin();it!=myVector.end();it++)
                                      cout<<*it<<" ";
                              cout <<endl;

                            }
                          }
                          else
                          {
                            if(n==8)
                            {
                              if(myVector.empty())
                                    cout<<"There are no elements in the vector. First create a vector! ";
                              else
                                  {
                                    myVector.clear();
                                    cout<<"The vector has been deleted";
                                  }
                            }
                            else
                                if(n==9)
                                {
                                  if(myVector.empty())
                                        cout<<"There are no elements in the vector.";
                                  else
                                        cout<<"There are elements in the vector.";
                                }
                                else
                                   if(n==0)
                                       break;
                                   else
                                    {
                                      if(n==10)
                                         {
                                           if(myVector.empty())
                                                cout<<"There are no elements in the vector. First create a vector! ";
                                           else
                                           {
                                              cout<<"Number of elements in the vector: "<<myVector.size();
                                              cout<<endl;
                                           }
                                         }
                                    }
                                       if(n<0||n>10)
                                             cout<<"Error! Select a number from the menu!";

                          }
                        }

      cout<<endl;
      cout<< "--------------------------"<<endl;
      cout <<"1 --- Creating a vector;"<<endl;
      cout<< "2 --- Inverting the elements of a vector;"<<endl;
      cout<< "3 --- Add an element to the end of a vector;"<<endl;
      cout<< "4 --- Remove the last element from the vector;"<<endl;
      cout<< "5 --- Change the content;"<<endl;
      cout<< "6 --- Insert in vector;"<<endl;
      cout<< "7 --- Delete an element from the vector;"<<endl;
      cout<< "8 --- Delete the vector;"<<endl;
      cout<< "9 --- I check if I have elements in the vector;"<<endl;
      cout<< "10--- I check how many elements the vector has;"<<endl;
      cout<< "0 --- Exit;"<<endl;
      cout<< "--------------------------"<<endl;
      cin>>n;
    }

    return 0;
}
