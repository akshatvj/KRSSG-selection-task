#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <bits/stdc++.h>
#include "opencv2/core/core.hpp"
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib> 
#include <ctime> 
#include <iostream>
#include<bits/stdc++.h> 
#include <time.h>
#include <fstream>
using namespace std;
using namespace cv;
Mat img =imread("image.png",1);
Mat img1 =imread("image.png",1);
float step = 5.00;
float radius = 70.00;
 struct node{
	int x;
	int y;
	int parent;
	float cost;	
};

float distance(node a,node b){
	return sqrt(pow(b.x - a.x, 2) + pow(a.y - b.y, 2));
}
node node1[5000020],node2[5000200],nowar[1000];
int l3 = 0;
int xmax=img.rows;
int ymax=img.cols;

node start(){
	srand(time(NULL));
 for (int i = 0; i < xmax; ++i)
 {for (int j = 0; j < ymax; ++j)
 	{if(img.at<Vec3b>(i,j)[0]< 100 &&img.at<Vec3b>(i,j)[1]>200 && img.at<Vec3b>(i,j)[2] <100){
 			node star;
 			star.x = i;
 			star.y = j;
 			star.cost = 0;
 			star.parent = -1;
 			return star;}}}}
 node end(){
 for (int i = 0; i < xmax; ++i)
 {for (int j = 0; j < ymax; ++j)
 	{if(img.at<Vec3b>(i,j)[0]< 100 &&img.at<Vec3b>(i,j)[2]>200 && img.at<Vec3b>(i,j)[1] <100){
 			node star;
 			star.x = i;
 			star.y = j;
 			star.cost = 0;
 			star.parent = -1;
 			return star;}}}}
int l1 =1,l2 = 1;
int near_node(node nodel[],node rnode,int len)
{
  float min_dist = 9999.0,dist;
  int lnode = 0, i = 0;
  for(i=0; i<len; i++)
  {
    dist = distance(nodel[i],rnode);
    if(dist<min_dist)
    {
      min_dist = dist;
      lnode = i;
    }
  }
  return lnode;
}
node ranode(){
	node rnode;
	rnode.x = rand()%(xmax);
	rnode.y = rand()%(ymax);
	return rnode;
}
int cheak(node nod1,node nod2){
if(nod1.x = nod2.x){
	int p,q;
if(nod1.y<nod2.y){
	 p=nod1.y,q=nod2.y;}
	else{
	 q=nod1.y,p=nod2.y;	
	}
	for (int u = p; u <q+1; ++u)
		{
		if(img1.at<Vec3b>(nod1.x,u)[0] > 100 &&img1.at<Vec3b>(nod1.x,u)[2]>100 && img1.at<Vec3b>(nod1.x,u)[1] >100){
  	return 0;}
  	if(img1.at<Vec3b>(nod1.x+10,u)[0] > 100 &&img1.at<Vec3b>(nod1.x+10,u)[2]>100 && img1.at<Vec3b>(nod1.x+10,u)[1] >100){
  	return 0;}
  	if(img1.at<Vec3b>(nod1.x-10,u)[0] > 100 &&img1.at<Vec3b>(nod1.x-10,u)[2]>100 && img1.at<Vec3b>(nod1.x-10,u)[1] >100){
  	return 0;}
  }
  	return 1;	
}

else{
	float slope = (float(nod1.y)-nod2.y)/(float(nod1.x)-nod2.x);
int p,q,py,qy;
if(nod1.x>nod2.x){
p=nod2.x,q=nod1.x;
py = nod2.y,qy = nod1.y;}
else{
q=nod2.x,p=nod1.x;
qy = nod2.y,py = nod1.y;}
for (int z = p; z <q+1 ; ++z)
{ int yp = int(slope*(z-p)+py);
  if(img1.at<Vec3b>(z,yp)[0] > 100 &&img1.at<Vec3b>(z,yp)[2]>100 && img1.at<Vec3b>(z,yp)[1] >100){
  	return 0;}
  	if(img1.at<Vec3b>(z+10,yp)[0] > 100 &&img1.at<Vec3b>(z+10,yp)[2]>100 && img1.at<Vec3b>(z+10,yp)[1] >100){
  	return 0;}
  	if(img1.at<Vec3b>(z-10,yp)[0] > 100 &&img1.at<Vec3b>(z-10,yp)[2]>100 && img1.at<Vec3b>(z-10,yp)[1] >100){
  	return 0;}
  }
  	return 1;}}
void twore(node n1,node n2,node n[],int w){
	if(n1.cost > n2.cost+distance(n1,n2) && cheak(n1,n2)){
		line(img, Point(n1.y, n1.x), Point((n[n1.parent]).y, (n[n1.parent]).x), Scalar(0, 0, 0), 1, 8);
		line(img, Point(n1.y, n1.x), Point(n2.y, n2.x), Scalar(255, 255, 255), 1, 8);
		n1.parent = w;
		n1.cost = n2.cost+distance(n1,n2);
	}

}
void rewireing(node list[],int len,int pos){
	float mind = 999999.0;
	int fp = -1;
	for (int ii = 0; ii < len; ++ii)
	{ if(ii!=pos && distance(list[ii],list[pos])<radius && mind >(list[ii].cost+distance(list[ii],list[pos])) &&(cheak(list[ii],list[pos]))){
		mind = (list[ii].cost+distance(list[ii],list[pos]));
		fp = ii;}}
		if(fp !=list[pos].parent){
			line(img, Point(list[pos].y, list[pos].x), Point(list[list[pos].parent].y, list[list[pos].parent].x), Scalar(0, 0, 0), 1, 8);
			list[pos].parent = fp;
			list[pos].cost = mind;
			line(img, Point(list[pos].y, list[pos].x), Point(list[fp].y, list[fp].x), Scalar(255, 255, 255), 1, 8);
			for (int iii = 0; iii < len; ++iii){
				if(iii!=pos && distance(list[iii],list[pos])<radius){
					twore(list[iii],list[pos],list,pos);
				}
			}
		
		}}

void newlink(node list[],int* le){
	int len = *le;
node renode = ranode();
int yy =near_node(list,renode,len);
float base =distance(list[yy],renode);
if(base){
list[len].x = int(list[yy].x + ((renode.x - list[yy].x)*step)/base);
list[len].y = int(list[yy].y + ((renode.y - list[yy].y)*step)/base);
list[len].parent = yy;
list[len].cost =  list[yy].cost + distance(list[yy],list[len]);
if(cheak(list[len],list[yy])){
line(img, Point(list[len].y, list[len].x), Point(list[yy].y, list[yy].x), Scalar(220, 123, 255), 1, 8);
(*le)++;
rewireing(list,len+1,len);
}}
return;}

void cheakend(node qw,node lis[],int len,node lis1[]){
	int uy = near_node(lis,qw,len);
	if(step>distance(lis[uy], qw)){
		node n01 = qw,n02 = lis[uy];
		line(img1, Point(n01.y, n01.x), Point(n02.y, n02.x), Scalar(255, 255, 255), 1, 8);
		while(n01.parent !=-1 ){
				nowar[l3] = n01;
				l3++;
				line(img1, Point(n01.y, n01.x), Point(lis1[n01.parent].y, lis1[n01.parent].x), Scalar(255, 255, 255), 1, 8);
			 n01= lis1[n01.parent];
			imshow("output",img1);
			 waitKey(100);}
			nowar[l3] = n01;
			l3++; 
		while(n02.parent !=-1 ){	 
			 if(n02.parent !=-1 ){
			 	nowar[l3] = n02;
				l3++;
				line(img1, Point(n02.y, n02.x), Point(lis[n02.parent].y, lis[n02.parent].x), Scalar(255, 255, 255), 1, 8);
			 n02= lis[n02.parent];}
			 imshow("output",img1);
			 waitKey(100);
			 }
		nowar[l3] = n02;
		l3++;
	step = 6.00;}
	return;}
bool comp(node n1,node n2){
	return(n1.x<n2.x);
}


int main()
{
	
cout<<xmax<<ymax;
namedWindow("output",0);
int t = 5000;
node2[0]  = end();
node1[0]  = start();
while (step == 5.00){
newlink(node1,&l1);
cheakend(node1[l1-1],node2,l2,node1);
newlink(node2,&l2);
cheakend(node2[l2-1],node1,l1,node2);
if(step!=5.00){
	break;
}
imshow("output",img);
waitKey(60000);}
imshow("output",img1);
waitKey(0);
sort(nowar, nowar+l3, comp);
ofstream myfile;
  myfile.open ("points.txt");
for (int iq = 0; iq < l3; ++iq)
{
cout << "[" << nowar[iq].x << "," << nowar[iq].y << "] ";
myfile << nowar[iq].x*11.00/xmax<<"\n"<< nowar[iq].y*11.0/ymax <<"\n";

}
myfile.close();
return 0;
}
