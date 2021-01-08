package day03;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int whiteCount=0;
	static int blueCount=0;

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();		
		int[][] arr = new int[N][N];
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++)
				arr[i][j]=sc.nextInt();
		}
		
		f(arr,N);
		
		System.out.println(whiteCount);
		System.out.println(blueCount);
	}
	
	public static void f(int[][] arr, int N) {
		
		// N의 크기가 1개일때, 탈출조건
		if(N==1) {
			if(arr[N-1][N-1]==1)
				blueCount++;
			else
				whiteCount++;
			
			return;
		}
		
		// 모두 파란색 종이일때, 탈출조건
		if(sum(arr,N)==N*N) {
			blueCount++;
			return;
		}
		
		// 모두 하얀색 종이일때, 탈출조건
		if(sum(arr,N)==0) {
			whiteCount++;
			return;
		}
		
		// Divide
		int[][] leftAndTop = new int[N/2][N/2];
		int[][] leftAndBottom = new int[N/2][N/2];
		int[][] rightAndTop = new int[N/2][N/2];
		int[][] rightAndBottom = new int[N/2][N/2];
		
		copy(arr,leftAndTop,0,0,N/2);
		copy(arr,rightAndTop,N/2,0,N/2);
		copy(arr,leftAndBottom,0,N/2,N/2);
		copy(arr,rightAndBottom,N/2,N/2,N/2);
		
		// Conquer
		f(leftAndTop,N/2);
		f(rightAndTop,N/2);
		f(leftAndBottom,N/2);
		f(rightAndBottom,N/2);
	}
	
	public static int sum(int[][] arr, int N) {
		
		int sum =0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++)
				sum+=arr[i][j];
		}
		return sum;
	}
	
	public static void copy(int[][] src, int[][] dest, int srcXPos, int srcYPos, int N) {
		
		int j=0;
		for(int i=srcYPos;i<srcYPos+N;i++) 
			System.arraycopy(src[i], srcXPos, dest[j++], 0, N);
	}
	

}
