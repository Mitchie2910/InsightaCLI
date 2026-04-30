
# InsightaCLI

InsightaCLI is a powerful command-line interface tool built in Python to interact seamlessly with the Insighta platform. It provides user authentication, advanced profile management capabilities, and supports exporting data with flexible filtering and sorting options. InsightaCLI makes it easy for both technical and non-technical users (via its complementary web portal) to explore, manage, and analyze social profiles effectively.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Authentication Commands](#authentication-commands)
  - [Profiles Commands](#profiles-commands)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Web Portal](#web-portal)

---

## Features

- Secure authentication with token storage and auto-refresh support.
- Manage user profiles: list, filter, search, get details, create, and export.
- Rich filtering: gender, country, age groups, and custom age ranges.
- Support for sorting and pagination.
- User-friendly output with structured tables and loading indicators.
- Clear error handling with actionable feedback.
- Export profile data as CSV files saved directly to the current directory.
- Complements a simple web portal for non-technical user access.

---

## Installation

InsightaCLI is available as a Python package and can be installed locally using pip:

```bash
pip install e .
```

> **Note:** This requires running the installation from within the InsightaCLI project directory where the setup files are located.

---

## Usage

All InsightaCLI commands follow the structure:

```bash
insighta <command> [subcommand] [options]
```

### Authentication Commands

Manage user sessions and credentials securely.

- **Login to Insighta**

```bash
insighta login
```

Logs in the user and saves tokens securely at `~/.insighta/credentials.json`.

- **Logout**

```bash
insighta logout
```

Clears stored authentication credentials.

- **Check current user**

```bash
insighta whoami
```

Displays the authenticated user's information.

### Profiles Commands

Interact with social profiles data with powerful filters and operations.

- **List profiles**

```bash
insighta profiles list
```

Lists all profiles in a paged table with default view.

- **Filter by gender**

```bash
insighta profiles list --gender male
```

- **Filter by country and age group**

```bash
insighta profiles list --country NG --age-group adult
```

- **Filter by custom age range**

```bash
insighta profiles list --min-age 25 --max-age 40
```

- **Sort list**

```bash
insighta profiles list --sort-by age --order desc
```

- **Pagination**

```bash
insighta profiles list --page 2 --limit 20
```

- **Get profile details by ID**

```bash
insighta profiles get <id>
```

- **Search profiles**

```bash
insighta profiles search "young males from nigeria"
```

- **Create a new profile**

```bash
insighta profiles create --name "Harriet Tubman"
```

- **Export profiles to CSV**

```bash
insighta profiles export --format csv
insighta profiles export --format csv --gender male --country NG
```

Exports the data as a CSV file saved directly to the current working directory.

---

## Configuration

- **Credential Storage:**  
  Authentication tokens are stored securely in `~/.insighta/credentials.json`.

- **Token Management:**  
  The CLI automatically handles token expiry: it attempts auto-refresh or prompts users to re-login if refresh fails.

- **Output:**  
  Results are displayed in structured tables with loading spinners shown during data fetch operations for enhanced user experience.

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository and create your feature branch:  
   `git checkout -b feature/YourFeature`

2. Commit your changes with clear descriptive messages:  
   `git commit -m "Add feature X"`

3. Push your branch to your fork:  
   `git push origin feature/YourFeature`

4. Create a pull request detailing your changes.

Please ensure your code adheres to PEP 8 standards and includes relevant tests when applicable.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---