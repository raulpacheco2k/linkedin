import json
import re
import unicodedata
from collections import Counter

# Carregar o arquivo JSON
with open("./linkedin/jobs_example.json", "r") as file:
    jobs = json.load(file)

# Definir as palavras-chave de tecnologia que queremos contar
technologies = [
    # Programming languages
    "Python", "Java", "Go", "JavaScript", "C++", "TypeScript", "PHP", "Ruby", "C", "C#", "Nix", "Shell",
    "Rust", "Scala", "Kotlin", "Swift", "Dart", "Groovy", "Perl", "Lua", "DM", "SystemVerilog",
    "Objective-C", "Elixir", "CodeQL", "OCaml", "Haskell", "PowerShell", "Erlang", "Emacs Lisp", "Julia",
    "Clojure", "CoffeeScript", "Verilog", "WebAssembly", "MLIR", "Bicep", "Fortran", "Cython", "GAP",
    "MATLAB", "Puppet", "JetBrains MPS", "Smalltalk", "Vala", "Haxe", "Pascal",

    # Java ecosystem
    "Selenium", "Rest Assured", "Cucumber", "AsserJ", "Hamcrest", "Serenity", "JBehave", "JUnit", "JUnitParams",
    "TestContainers", "Selenide", "Mockito", "TestNG", "Pact", "Appium", "Awaitility", "Arquillian", "Spock",
    "WireMock", "Spring Test", "Gatling", "Powermock", "Jacoco", "GEB", "Karate", "Restlet", "Jmeter", "JMockit",
    "Checkstyle", "JProfiler", "Maven", "Gradle", "Hibernate", "Spring", "Quarkus",

    # JavaScript ecosystem
    "Cypress", "Puppeteer", "Playwright", "Jasmine", "Jest", "Mocha", "ESLint", "Nightwatch", "Protractor", "QUnit",
    "Chai", "Npm", "yarn", "Node", "Express", "Nest", "React", "Angula", "Vue", "Tailwind", "Vite", "Ionic",
    "Prisma.io", "Sails", "Meteor", "Fastify",

    # Python ecosystem
    "unittest", "pytest", "nose2", "doctest", "Robot Framework", "Behave", "Django", "Flask", "FastAPI", "Bottlepy",
    "SQLAlchemy", "Tkinker", "Tensor Flow", "PyTorch", "OpenCV", "Numpy", "Scrapy", "Sympy", "Streamlit", "Seaborn",
    "Matplotlib", "Pandas",

    # PHP ecosystem
    "PHPUnit", "Pest", "Dusk", "Composer", "Laravel", "Slim", "Lumem", "Leaf MVC",

    # Práticas de Teste
    "TDD", "BDD",

    # Tools
    "Allure", "Jenkins", "TestComplete", "Postman", "Docker", "Git", "Swagger", "Apache Kafka", "RabbitMQ", "IBM RPA",
    "Power Plataform", "Power Automate",

    # Static analysis
    "SonarQube", "CodeScene",

    # Track
    "Jira", "Gitlab", "Github",

    # Database
    "MySQL", "PostgreSQL", "MongoDB", "Firebase", "SQLite", "SQL Server", "Redis", "Dynamo", "RDS",

    # Cloud
    "AWS", "Azure", "GCP", "IBM Cloud", "Oracle Cloud", "Alibaba Cloud", "DigitalOcean", "Heroku", "Netlify", "Vercel",

    # Host
    "Hostinger", "GoDaddy", "HostGator",

    # Docs
    "Confluence",

    # Test Management
    "Xray", "TestRail", "TestLink", "Bugzilla", "Redmine", "Mantis", "Qase",

    # Others
    "Scrum", "Kanban", "Bootstrap", "MVC", "MVVM", "MVP", "DevOps",

    # Languages
    "Inglês", "Espanhol", "Francês", "Italiano",

    # College
    "Graduação", "Pós-graduação", "MBA", "Mestrado", "Doutorado",

    # Certifications
    "CPRE-FL", "CPRE-AL", "CPRE-AL", "CPRE-AL", "CPRE-FL", "CPRE-AL", "CTFL", "CTAL-TM", "CTAL-TA", "CTAL-TTA",
    "CTAL-TAE", "CTFL-AT", "CTAL-ATT", "CT-ATLaS", "CT-AcT", "CT-AI", "CT-GaMe", "CT-GT", "CT-MAT", "CT-MBT", "CT-PT",
    "CT-SEC", "CT-TAE", "CT-TAS", "CT-UT",

    # Seniority
    "Júnior", "Pleno", "Sênior"
]

# Inicializar um contador para as tecnologias
tech_counter = Counter()


# Função para encontrar correspondências exatas de palavras
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def find_exact_match(text, keyword):
    # Remover acentos e converter para minúsculas
    normalized_text = remove_accents(text).lower()
    normalized_keyword = remove_accents(keyword).lower()

    # Criar um padrão de expressão regular para encontrar palavras exatas
    pattern = r'(?<!\w)' + re.escape(normalized_keyword) + r'(?!\w)'
    return re.search(pattern, normalized_text) is not None


# Contar a frequência de cada tecnologia nas descrições das vagas
for job in jobs:
    job_description = job.get("job_description")
    for tech in technologies:
        if find_exact_match(job_description, tech):
            tech_counter[tech] += 1

# Converter o contador em uma lista de tuplas e ordená-la
tech_counts = sorted(tech_counter.items(), key=lambda x: x[1], reverse=True)
# tech_counts = dict(tech_counter)

# Exibir os resultados
print(tech_counts)
