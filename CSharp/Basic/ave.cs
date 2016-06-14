using System;

namespace Test
{
	class Program
	{
		static void Main(string[] args)
		{
			double[] data = { 5.1,4.2,3.1,2.2,1.4 };
			double sum=0,ave=0; //  合計値, 平均値の格納用
			// 合計を計算
			for(int i = 0; i < data.Length; i++){
				sum += data[i];
			}
			ave = sum / data.Length;
			Console.WriteLine("平均値：" + ave);
		}
	}
}
