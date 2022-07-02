#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    cout<< "--------------------------"<<endl;
    cout<< "1 --- Crearea unui vector;"<<endl;
    cout<< "2 --- Inversarea elementelor unui vector;"<<endl;
    cout<< "3 --- Adauga un element la sfarsitul unui vector;"<<endl;
    cout<< "4 --- Elimina ultimul element din vector;"<<endl;
    cout<< "5 --- Schimba continutul;"<<endl;
    cout<< "6 --- Insereaza in vector;"<<endl;
    cout<< "7 --- Sterge un element din vector;"<<endl;
    cout<< "8 --- Sterge vectorul;"<<endl;
    cout<< "9 --- Verific daca am elemente in vector;"<<endl;
    cout<< "10--- Verific cate elemente are vectorul;"<<endl;
    cout<< "0 --- Iesire;"<<endl;
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
        cout<<"Alege dimensiunea vectorului: ";
        cin>>dim;
        cout<<"Introdu elementele vectorului: ";
        for(i=0;i<dim;i++)
        {
          cin>>elem;
          myVector.push_back(elem);
        }
        cout<<endl;
        cout << "Acesta este vectorul nostru: ";
        for(it=myVector.begin();it!=myVector.end();it++)
                   cout<<*it<<" ";
        cout <<endl;
      }
      else
          if(n==2)
          {
            if(myVector.empty())
               cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
            else
               {
                 reverse(myVector.begin(),myVector.end());
                 cout<<"Vectorul dupa inversare: "<<endl;
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
                      cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
               else
                {
                  cout<<"Elementul pe care il adaugi:";
                  cin>>nr;
                  myVector.push_back(nr);
                  cout<<"Vectorul dupa adaugare: "<<endl;
                  for(it=myVector.begin();it!=myVector.end();it++)
                            cout<<*it<<" ";
                  cout <<endl;
                }
              }
              else
                 if(n==4)
                 {
                   if(myVector.empty())
                         cout<<"Nu exista elemente in vector. Intai creeaza un vector! "<<endl;
                   else
                   {
                     myVector.pop_back();
                  cout<<"Vectorul dupa eliminarea ultimului element: "<<endl;
                  for(it=myVector.begin();it!=myVector.end();it++)
                            cout<<*it<<" ";
                  cout <<endl;
                   }
                 }
                 else
                    if(n==5)
                    {
                      if(myVector.empty())
                            cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
                      else
                      {
                        vector<int>Vector;
                        vector<int>::iterator ite;
                        cout<<"Al doilea vector: "<<endl;
                        int dimen, element;
                        cout<<"Alege dimensiunea vectorului: ";
                        cin>>dimen;
                        cout<<"Introdu elementele vectorului: ";
                        for(i=0;i<dimen;i++)
                        {
                            cin>>element;
                            Vector.push_back(element);
                        }
                        cout<<endl;
                        cout << "Acesta este al doilea vector al nostru: ";
                        for(ite=Vector.begin();ite!=Vector.end();ite++)
                                 cout<<*ite<<" ";
                        cout <<endl;
                        cout <<endl;

                        cout << "Acesta este primul vector al nostru: ";
                        for(it=myVector.begin();it!=myVector.end();it++)
                                 cout<<*it<<" ";
                        cout <<endl;
                        cout <<endl;

                        Vector.swap(myVector);
                        cout<<"Dupa schimbarea continutului:"<<endl;
                        cout <<endl;
                        cout << "Acesta este primul vector al nostru: ";
                        for(it=myVector.begin();it!=myVector.end();it++)
                                 cout<<*it<<" ";
                        cout <<endl;
                        cout <<endl;
                        cout << "Acesta este al doilea vector al nostru: ";
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
                                cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
                          else
                          {
                            cout<<"Creeaza un vector:"<<endl;
                            vector<int>anothervector;
                            vector<int>::iterator y;
                            int di, el;
                        cout<<"Alege dimensiunea vectorului: ";
                        cin>>di;
                        cout<<"Introdu elementele vectorului: ";
                        for(i=0;i<di;i++)
                        {
                            cin>>el;
                            anothervector.push_back(el);
                        }
                        cout<<endl;
                        cout<<"Acesta este al doilea vector al nostru: ";
                        for(y=anothervector.begin();y!=anothervector.end();y++)
                                 cout<<*y<<" ";
                        cout <<endl;
                        cout<<"Alege din ce pozitie sa se insereze: ";
                        int m;
                        cin>>m;
                        y=myVector.begin();
                        myVector.insert(y+m,anothervector.begin(),anothervector.end());
                        cout<<"Vectorul nostru dupa insert: ";
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
                                cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
                            else
                            {
                              cout<<"Alege care element sa fie sters: "<<endl;
                              cout<<"pozitia=";
                              int pozitie;
                              cin>>pozitie;
                              myVector.erase(myVector.begin()+pozitie);
                              cout <<endl;
                              cout<<"Noul vector dupa stergere: ";
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
                                    cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
                              else
                                  {
                                    myVector.clear();
                                    cout<<"S-a sters vectorul";
                                  }
                            }
                            else
                                if(n==9)
                                {
                                  if(myVector.empty())
                                        cout<<"Nu exista elemente in vector.";
                                  else
                                        cout<<"Exista elemente în vector.";
                                }
                                else
                                   if(n==0)
                                       break;
                                   else
                                    {
                                      if(n==10)
                                         {
                                           if(myVector.empty())
                                                cout<<"Nu exista elemente in vector. Intai creeaza un vector! ";
                                           else
                                           {
                                              cout<<"Numarul de elemente din vector: "<<myVector.size();
                                              cout<<endl;
                                           }
                                         }
                                    }
                                       if(n<0||n>10)
                                             cout<<"Eroare! Selecteaza un numar din meniu!";

                          }
                        }

      cout<<endl;
      cout<< "--------------------------"<<endl;
      cout <<"1 --- Crearea unui vector;"<<endl;
      cout<< "2 --- Inversarea elementelor unui vector;"<<endl;
      cout<< "3 --- Adauga un element la sfarsitul unui vector;"<<endl;
      cout<< "4 --- Elimina ultimul element din vector;"<<endl;
      cout<< "5 --- Schimba continutul;"<<endl;
      cout<< "6 --- Insereaza in vector;"<<endl;
      cout<< "7 --- Sterge un element din vector;"<<endl;
      cout<< "8 --- Sterge vectorul;"<<endl;
      cout<< "9 --- Verific daca am elemente in vector;"<<endl;
      cout<< "10--- Verific cate elemente are vectorul;"<<endl;
      cout<< "0 --- Iesire;"<<endl;
      cout<< "--------------------------"<<endl;
      cin>>n;
    }

    return 0;
}
