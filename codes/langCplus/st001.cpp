#include <iostream>
/*
 * Wandeson Ricardo
 * st{n} -> n=001,002,...,999
 * Códigos e estudos (Study + Testes).
 * Básico de classes e variaveis, e I/O
 */
using namespace std;
class Animal {
public:
    string nome;
    int idade;
    float peso;
    string especie;
// Methods
public:    
    Animal(string nm, int ida , float pes, string spe ){
        nome = nm;
        idade = ida;
        peso = pes;
        especie = spe;
    }
    
    
};
class Complex {
public:
    double real, imag;
    //static const double i2 = -1.0;
public:
    Complex(double r, double im);
    Complex add(Complex z1, Complex z2);
    Complex sub(Complex z1, Complex z2);
    Complex prod(Complex z1, Complex z2);
    ~Complex();
};

Complex::Complex(double r, double im) {
    real = r; imag = im;
}

Complex Complex::add(Complex z1, Complex z2) {
    Complex z(0,0);
    z.real = z1.real + z2.real; z.imag = z1.imag + z2.imag;
    return z;
    
}
Complex Complex::sub(Complex z1, Complex z2) {
    Complex z(0,0);
    z.real = z1.real + z2.real; z.imag = z1.imag + z2.imag;
    return z;
}
Complex Complex::prod(Complex z1, Complex z2) {
}
Complex::~Complex(){
   // cout<<"\nDestroyed objects..."<<endl;
}
int main(void){
    Animal dog("Fred", 4, 7.0, "cao");
    int h = 0x45;
    //dog.nome = "Fred2";
    cout << "Test " << dog.nome << endl;
    // std::hex show hexadecimal variable in base 16, 0xn where n in set {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
    cout << "Hex "<< std::hex << h << " In dec " << std::dec << h <<endl;
    cout << "Hex " << std::hex << ++h << endl; // ++h is different of h++ . ++h -> 46 and h++ -> 45
    
    // Numbers complex
    Complex z(2.0, 1.0);
    Complex z1(3.0, 5.0);
    cout<<"Complex number \n \tz = \n\t\t" << z.imag << ", " <<z.real<<"i"<<endl;
    cout<<"Complex number \n \tz1 = \n\t\t" << z1.imag << ", " <<z1.real<<"i"<<endl;
    z1 = z.add(z,z1);
    cout<<"Complex number \n \tz1 = \n\t\t" << z1.imag << ", " <<z1.real<<"i"<<endl;
      

    return 0;
}
