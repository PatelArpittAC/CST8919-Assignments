### Both Assignment-1 and Assignment-2 are present in this repository as previewed
```
---o---o---o---> /Assignment-1             branch : main
            \
             o---o---> /Assignment-2       branch : Assignment-2
``` 

# Assignment-2
### Automating Anomaly Detection and Alerting in Cloud Security

## Team Members:

- Arpit Patel (041080697)
- Meet Dewani (041050046)
- Kalpitkumar Parekh (041093041)
- Devansh Sheth (041091741)

## Project Structure

```
├──Assignment-1
├──Assignment-2
│    ├── Images
│    │   └── (contains 26 '.png' images)
│    └── README.md
├── .gitignore
└── LICENSE

1 directory, 1 file in Assignment-2 (excluding Images)
```

## Setup instructions:

### Part 1: Understanding Anomaly Detection

Detecting anomalies in security log analysis is vital for spotting unusual patterns or behaviors that stray from the usual, which could signal security threats like cyberattacks, system glitches, or unauthorized entry. These methods rely on data analytics, machine learning, and statistical approaches to keep tabs on, identify, and address anomalies within large, intricate datasets produced by IT systems and applications. This report briefly outlines some of the most potent anomaly detection methods relevant to security log analysis:

Anomaly detection methods can be broadly classified into the following categories:

1. Statistical Approaches: These methods operate under the assumption that regular behavior adheres to a clearly defined statistical distribution. Any significant deviation from this distribution indicates an anomaly. Techniques encompass:

- Supervised learning (e.g., utilizing labeled data to train models on recognized anomalies)
- Unsupervised learning (e.g., employing clustering algorithms like K-means or DBSCAN)
- Semi-supervised learning (combining both labeled and unlabeled data)

2. Rule-Based Approaches: These methods entail establishing explicit rules that delineate normal behavior. Any behavior contravening these rules is flagged as an anomaly. While this method is straightforward, it necessitates extensive domain knowledge to formulate accurate rules.

### Part 2: Preparing for Automation Azure Automation Account Setup
### Part 3: Implementing Anomaly Detection
### Part 4: Integrating Cloud Security Best Practices

---

1. Kubernetes Application Setup: This stage involved deploying an application within a Kubernetes cluster using a `service.yaml` and `deployment.yaml` file to execute a Docker image. This process ensures the proper containerization and hosting of the application within the Kubernetes environment.
2. Google SSO Implementation: We incorporated Google SSO to establish an authentication mechanism, allowing users to log in using their Gmail accounts, thereby bolstering security and user management.
3. Syslog Server Setup: A Syslog server was configured, and the application was configured to transmit logs to this server. This centralized logging and monitoring setup offers insights into application behavior and potential security incidents.
4. Integration with Azure Log Analytics: We executed steps to establish a Log Analytics Workspace, connect a virtual machine to Azure via Azure Arc, and create a data collection rule. This facilitates querying of Google SSO App logs within Azure Log Analytics, providing advanced monitoring and analysis capabilities.
5. Data Visualization using Grafana: Lastly, we installed and configured Grafana on a virtual machine, including tasks such as app registration, permission settings for Log Analytics API, client secret creation, and access control setup. This integration enables Grafana to connect to Azure Log Analytics Workspace and create dashboards for visualizing authentication attempts and other crucial data.

## Steps Performed


## Conclusion


---

- GitHub Repo:
[PatelArpittAC/CST8919-Assignments](https://github.com/PatelArpittAC/CST8919-Assignments)
