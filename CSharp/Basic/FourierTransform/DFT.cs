// C#言語で逆フーリエ変換をする
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

        /// <summary>
        /// 離散フーリエ変換
        /// </summary>
        static void DiscreteFourierTransform(
            double[] inputRe, out double[] outputRe, out double[] outputIm)
        {
            int size = inputRe.Length;

            outputRe = new double[size];
            outputIm = new double[size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    outputRe[i] +=
                        inputRe[j] *
                        Math.Cos(
                            2.0 * Math.PI * (double)j *
                            (double)i /
                            (double)size
                        );
                    outputIm[i] -=
                        inputRe[j] *
                        Math.Sin(
                            2.0 * Math.PI * (double)j *
                            (double)i /
                            (double)size
                        );
                }
            }
        }

        /// <summary>
        /// 逆フーリエ変換
        /// </summary>
        static void InverseFourierTransform(
            double[] inputRe, double[] inputIm, out double[] outputRe)
        {
            int size = inputRe.Length;
            outputRe = new double[size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    outputRe[i] +=
                        inputRe[j] *
                        Math.Cos(
                            2.0 * Math.PI * (double)j *
                            (double)i /
                            (double)size)
                        - inputIm[j] *
                        Math.Sin(
                            2.0 * Math.PI * (double)j *
                            (double)i /
                            (double)size
                        );
                }
                outputRe[i] /= size;
            }
        }
    }
}
