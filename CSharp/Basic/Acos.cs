using System;

namespace Test
{
	class Program
	{
		static void Main(string[] args)
		{
			double deg = 30;
			double rad = System.Math.PI * deg / 180.0;
			double y = System.Math.Acos(rad);
			Console.WriteLine("計算結果：" + y);
		}
	}
}
