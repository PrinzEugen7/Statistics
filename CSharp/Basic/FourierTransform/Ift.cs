using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace InverseFourierTransform
{
    class Program
    {
        static void Main(string[] args)
        {
            const int SIZE = 256;

            double[] data = new double[SIZE];
            double[] re;
            double[] im;

            // 初期化、適当な値でテスト
            for (int i = 0; i < SIZE; i++)
            {
                data[i] = i;
            }

            // 離散フーリエ変換
            DiscreteFourierTransform(data, out re, out im);
            // 逆フーリエ変換
            InverseFourierTransform(re, im, out data);

            // 出力
            for (int i = 0; i < SIZE; i++)
            {
                Console.WriteLine("{0} {1} {2}", data[i], re[i], im[i]);
            }
        }

        static void DiscreteFourierTransform(double[] Re1, out double[] Re2, out double[] Im2)
        {
            int size = Re1.Length;
            Re2 = new double[size];
            Im2 = new double[size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Re2[i] += Re1[j] * Math.Cos(2.0 * Math.PI * (double)j * (double)i / (double)size);
                    Im2[i] -= Re1[j] * Math.Sin(2.0 * Math.PI * (double)j *(double)i/(double)size);
                }
            }
        }

        static void InverseFourierTransform( double[] Re1, double[] Im1, out double[] Re2)
        {
            int size = Re1.Length;
            Re2 = new double[size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Re2[i] += Re1[j] * Math.Cos(2.0 * Math.PI * (double)j * (double)i / (double)size)
                            - Im1[j] * Math.Sin(2.0 * Math.PI * (double)j * (double)i /(double)size);
                }
                Re2[i] /= size;
            }
        }
    }
}
