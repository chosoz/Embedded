#include "reg52.h"

//宏定义
#define uchar unsigned char
#define uint  unsigned int

//按键定义
sbit KEY1= P2^0;
sbit KEY2= P2^1;
sbit KEY3= P2^2;
sbit KEY4= P2^3;

//液晶控制引脚定义
sbit RS= P2^5;
sbit RW= P2^6;
sbit EN= P2^7;

//DAC定义
sbit  CS_5615=P1^5;
sbit CLK_5615=P1^6;
sbit DAT_5615=P1^7;

//ADC定义
sbit  CS=P3^5;       
sbit CLK=P3^3;      
sbit DIO=P3^4; 
//报警指示定义 
sbit led= P3^1; 

uint  U; 
uchar GETU=0;
bit flag=0;
uint  a=0;
unsigned long sumi=0;
unsigned int I_num;

uchar code tab1[]={"Welcome to use  "}; 	//固定字符
uchar code tab2[]={"adj power supply"};		//固定字符
uchar code tab3[]={"Voltage:     . V"};		//固定字符
uchar code tab4[]={"Electricity: . A"};		//固定字符
uchar code tab5[]={"                "};		//固定字符
uchar code tab6[]={"Short circuit!!!"};		//固定字符
uchar code tab7[]={"Please restart!!"};		//固定字符
//延时函数，后面经常调用
void delay(uint xms)//延时函数，有参函数
{
	uint x,y;
	for(x=xms;x>0;x--)
	 for(y=121;y>0;y--);
}

/********液晶写入指令函数与写入数据函数，以后可调用**************/

/*在这个程序中，液晶写入有关函数会在DS1302的函数中调用，所以液晶程序要放在前面*/

void write_1602com(uchar com)//****液晶写入指令函数****
{
	RS=0;//数据/指令选择置为指令
	RW=0; //读写选择置为写
	P0=com;//送入数据
	delay(1);
	EN=1;//拉高使能端，为制造有效的下降沿做准备
	delay(1);
	EN=0;//en由高变低，产生下降沿，液晶执行命令
}


void write_1602dat(uchar dat)//***液晶写入数据函数****
{
	RS=1;//数据/指令选择置为数据
	RW=0; //读写选择置为写
	P0=dat;//送入数据
	delay(1);
	EN=1; //en置高电平，为制造下降沿做准备
	delay(1);
	EN=0; //en由高变低，产生下降沿，液晶执行命令
}


void lcd_init()//***液晶初始化函数****
{
	uchar p;
	write_1602com(0x38);//设置液晶工作模式，意思：16*2行显示，5*7点阵，8位数据
	write_1602com(0x0c);//开显示不显示光标
	write_1602com(0x06);//整屏不移动，光标自动右移
	write_1602com(0x01);//清显示

	write_1602com(0x80);//日历显示固定符号从第一行第1个位置之后开始显示
	for(p=0;p<16;p++)
	{
		write_1602dat(tab1[p]);//向液晶屏写日历显示的固定符号部分
	}
	write_1602com(0xc0);//时间显示固定符号写入位置，从第2个位置后开始显示
	for(p=0;p<16;p++)
	{
		write_1602dat(tab2[p]);//写显示时间固定符号，两个冒号
	}
	delay(1000);
	write_1602com(0x80);//日历显示固定符号从第一行第1个位置之后开始显示
	for(p=0;p<16;p++)
	{
		write_1602dat(tab3[p]);//向液晶屏写日历显示的固定符号部分
	}
	write_1602com(0xc0);//时间显示固定符号写入位置，从第2个位置后开始显示
	for(p=0;p<16;p++)
	{
		write_1602dat(tab4[p]);//写显示时间固定符号，两个冒号
	}
}

void  shuma(uint buf)
{
	uchar a,b,c,d,p;
	a=buf/1000;
	b=buf%1000/100;
	c=buf%100/10;
	d=buf%10;
	if(flag==0)
	{
		write_1602com(0x80+11);
		if(a!=0)
		write_1602dat(a+0x30);
		else
		write_1602dat(' ');
		write_1602dat(b+0x30);
		write_1602dat('.');
		write_1602dat(c+0x30);
	}
	if(flag==1)
	{
		write_1602com(0x80);//时间显示固定符号写入位置，从第2个位置后开始显示
		for(p=0;p<16;p++)
		{
			write_1602dat(tab6[p]);//写显示时间固定符号，两个冒号
		}
		write_1602com(0xc0);//时间显示固定符号写入位置，从第2个位置后开始显示
		for(p=0;p<16;p++)
		{
			write_1602dat(tab7[p]);//写显示时间固定符号，两个冒号
		}
	}
}

void dis_electricity(uint buf)
{
	uchar a,b;
	a=buf%100/10;
	b=buf%10;
	if(flag==0)
	{
		write_1602com(0x80+0x40+12);
		write_1602dat(a+0x30);
		write_1602dat('.');
		write_1602dat(b+0x30);
	}
}

void tlc_5615(uint buf)
{
	uint a,c;
	c=buf;    
    CS_5615=0; 
	for(a=16;a>0;a--)
	{
         DAT_5615=c>>15;      
         c=c<<1;
         CLK_5615=1;
         CLK_5615=0;	         
    }
	CLK_5615=1;
	CLK_5615=0;
	CLK_5615=1;
	CLK_5615=0;
	CS_5615=1;
}

unsigned int  A_D()
{
	unsigned char i,dat;
	CS=1;   //一个转换周期开始
	CLK=0;  //为第一个脉冲作准备
	CS=0;  //CS置0，片选有效
	
	DIO=1;    //DIO置1，规定的起始信号  
	CLK=1;   //第一个脉冲
	CLK=0;   //第一个脉冲的下降沿，此前DIO必须是高电平
	DIO=1;   //DIO置1， 通道选择信号  
	CLK=1;   //第二个脉冲，第2、3个脉冲下沉之前，DI必须跟别输入两位数据用于选择通道，这里选通道CH0 
	CLK=0;   //第二个脉冲下降沿 
	DIO=0;   //DI置0，选择通道0
	CLK=1;    //第三个脉冲
	CLK=0;    //第三个脉冲下降沿 
	DIO=1;    //第三个脉冲下沉之后，输入端DIO失去作用，应置1
	CLK=1;    //第四个脉冲
	for(i=0;i<8;i++)  //高位在前
	{
		CLK=1;         //第四个脉冲
		CLK=0; 
		dat<<=1;       //将下面储存的低位数据向右移
		dat|=(unsigned char)DIO; 	 //将输出数据DIO通过或运算储存在dat最低位 
	}	  		        
	CS=1;          //片选无效 
	return dat;	 //将读出的数据返回     
}

void KEY()
{
	if(flag==0)
	{
		if(KEY1==0)
		{
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			if(KEY1==0)
			{
				if(U<900)	//1V对应的是80  10位ad
				U=U+6;
			}	
		}
		if(KEY2==0)
		{
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			if(KEY2==0)
			{
				if(U>=6)
				U=U-6;
			}	
		}			
		if(KEY3==0)
		{
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			if(KEY3==0)
			{
				U=300;	
			}	
		}	
		if(KEY4==0)
		{
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			shuma(U/6*10);
			if(KEY4==0)
			{
				U=0;
			}	
		}
	}
}


 //主函数
void main(void)
{
	uchar p;
	U=0;
	lcd_init();
	while(1)
	{
		for(p=0;p<20;p++)
		{
			GETU = A_D();
			sumi=sumi+GETU;
			delay(10);
			tlc_5615(U);
			shuma(U/6*10);
			dis_electricity(I_num);
			KEY();
			if(GETU>=13)   //0.0196V
			{
				U=0;
				led=0;
				a=0;
				flag=1;
			}
		}
		GETU=sumi/20;
		I_num=GETU*2;
		sumi=0;
	}
}

