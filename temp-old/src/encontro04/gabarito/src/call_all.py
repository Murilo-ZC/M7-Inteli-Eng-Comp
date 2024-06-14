# Implementa o pipeline de ETL dos dados
import extract
import transform

if __name__ == "__main__":
    extract.main()
    transform.main()