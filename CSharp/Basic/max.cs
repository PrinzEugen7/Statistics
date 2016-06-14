using System;
using System.Linq;

namespace Test
{
	class Program
	{
		static void Main(string[] args)
		{
			double[] data = { 5.1,4.2,3.1,2.2,1.4 };
			double max = data.Max();
			Console.WriteLine("最大値：" + max);
		}
	}
}
