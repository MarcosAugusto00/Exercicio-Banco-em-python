# main.py
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Processamento.Interface import run_interface

def main():
    run_interface()

if __name__ == "__main__":
    main()
