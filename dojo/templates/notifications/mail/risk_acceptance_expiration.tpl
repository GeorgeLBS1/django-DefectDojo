{% load i18n %}
{% load navigation_tags %}
{% load display_tags %}
{% url 'view_risk_acceptance' risk_acceptance.engagement.id risk_acceptance.id as risk_acceptance_url %}
{% url 'view_product' risk_acceptance.engagement.product.id as product_url %}
{% url 'view_engagement' risk_acceptance.engagement.id as engagement_url %}

<!DOCTYPE html>
<html lang="pl">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="X-UA-Compatible" content="ie=edge" />
		<title>Activation</title>

		<style>
			.proton-body {
				display: block;
				padding: 0px;
				margin: 0px;
			}

			.body-margin{
				padding-top: 100px;
				padding-left: 20px;
			}

			.proton-wrapper {
				width: 100%;
				display: block;
				overflow: hidden;
				box-sizing: border-box;
				color: #000000;
				background: #ffffff;
				font-size: 18px;
				font-weight: normal;
				font-family: 'Baloo 2', 'Open Sans', 'Roboto', 'Segoe UI', 'Helvetica Neue', Helvetica, Tahoma, Arial, monospace, sans-serif;
			}

			.proton-table {
				border-collapse: collapse;
				border-spacing: 0;
				border: 0px;
				width: 640px;
				max-width: 90%;
				margin: 100px auto;
				border-radius: 10px;
				overflow: hidden;
                padding: 0px;
				box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
			}

			.proton-table tr {
				background: #ffffff;
			}

			.proton-table td,
			.proton-table th {
				border: 0px;
				border-spacing: 0;
				border-collapse: collapse;
			}

			.proton-table tr td {
				padding: 0px 40px;
				box-sizing: border-box;
				padding: 0px;
			}

			.proton-margin-header {
                float: left;
                width: 100%;
                overflow: hidden;
                height: 70px;
                background-color: #000508;
                padding-bottom: 0px;
                box-sizing: border-box;
				border-bottom: 8px solid #06a2b7;
            }
			.proton-margin-bottom {
                float: left;
                width: 100%;
                overflow: hidden;
                height: 70px;
                background-color: #000508;
                padding-bottom: 0px;
                box-sizing: border-box;
            }

			.proton-div {
				float: left;
				width: 100%;
				overflow: hidden;
				box-sizing: border-box;
			}

			.proton-table h1,
			.proton-table h2,
			.proton-table h3,
			.proton-table h4 {
				float: left;
				width: 100%;
				margin: 0px 0px 20px 0px !important;
				padding: 0px;
			}

			.proton-table h1 {
                font-size: 33px;
                color: #ebf1ff;
                padding: 20px;
            }

			.proton-table h2 {
				font-size: 26px;
			}

			.proton-table h3 {
				font-size: 23px;
			}

			.proton-table p {
				float: left;
				width: 100%;
				font-size: 18px;
				margin: 0px 0px 20px 0px !important;
			}

			.proton-table h4 {
				font-size: 20px;
			}

			.proton-table a {
				color: #6d49fc;
				font-weight: bold;
			}

			.proton-table a.proton-link {
				display: inline-block;
				width: auto !important;
				outline: none !important;
				text-decoration: none !important;
			}

			.proton-table img,
			.proton-table a img {
				display: block;
				max-width: 100%;
				margin-bottom: 20px;
				border: 0px;
				border-radius: 10px;
				overflow: hidden;
			}

			.proton-table a.proton-button {
				display: inline-block;
				font-weight: bold;
				font-size: 17px;
				padding: 15px 40px;
				margin: 20px 0px;
				color: #040404 !important;
				background: #16cdfb !important;
				border-radius: 10px;
				text-decoration: none;
				outline: none;
			}

			.proton-table a.proton-button:hover {
				color: #000000  !important;
				background: #04f19a !important;
			}

			.proton-flex {
				float: left;
				width: 100%;
				text-align: center;
			}

			.proton-divider {
				float: left;
				width: 100%;
				overflow: hidden;
				margin: 20px 0px;
				border-top: 2px solid #f2f2fd;
			}
		</style>

		<style>
			.proton-flex img {
				margin: 10px;
				max-width: 15%;
				width: 40px;
			}
		</style>
	</head>

	<body class="proton-body">
		<div class="proton-wrapper">
			<table class="proton-table">
				<tbody>
                    {% autoescape on %}
					<tr class="proton-tr">
						<td class="proton-td" colspan="10" style="">
							<div class="proton-margin-header">
                                <h1>{{ system_settings.team_name }}</h1>
							<div class="proton-line" style="red">
								rene
							</div>
                            </div>
							<div class="body-margin">
								<h2>{% trans "Hello, " %}{{user.first_name}}</h2>
								<p>
									<b>{{ owner }}</b> {{ description|safe }}
									<br>
                                    <br>
                                        {% if risk_acceptance.is_expired %}
                                            {% blocktranslate with risk_url=risk_acceptance_url|full_url risk_findings=risk_acceptance.accepted_findings.all|length risk_date=risk_acceptance.expiration_date_handled|date %}<a href="{{risk_url}}">Risk acceptance {{ risk_acceptance }}</a> with {{ risk_findings }} findings has expired {{ risk_date }}{% endblocktranslate %}
                                        {% else %}
                                            {% blocktranslate with risk_url=risk_acceptance_url|full_url risk_findings=risk_acceptance.accepted_findings.all|length risk_date=risk_acceptance.expiration_date|date %}<a href="{{risk_url}}">Risk acceptance {{ risk_acceptance }}</a> with {{ risk_findings }} findings will expire {{ risk_date }}{% endblocktranslate %}
                                        {% endif %}
                                        <br/>
                                        {% if risk_acceptance.reactivate_expired %}
                                            <p>{% blocktranslate %}Findings have been reactivated</p>{% endblocktranslate %}
                                        {% endif %}
                                        <br/>
                                        {% if risk_acceptance.restart_sla_expired %}
                                            <p>{% blocktranslate %}Findings SLA start date have been reset</p>{% endblocktranslate %}
                                        {% endif %}
                                        <br/>
                                        <p>
                                            {% trans "Findings" %}:
                                            <br/>
                                            {% for finding in risk_acceptance.accepted_findings.all %}
                                                {% url 'view_finding' finding.id as finding_url %}
                                                <a href="{{ finding_url|full_url }}">{{ finding.title }}</a> ({{ finding.severity }}) {{ finding.status }}<br/>
                                            {% empty %}
                                                {% trans "None" %}<br/>
                                            {% endfor %}
                                        </p>
                                        <br/><br/>
                                        <b>{% trans "Kind regards" %},</b>
                                        <br/><br/>
                                                Devsecops
                                        <br/>
                                        <br/>
                                        </p>
                                        {% if system_settings.disclaimer and system_settings.disclaimer.strip %}
                                            <br/>
                                            <div style="background-color:#DADCE2; border:1px #003333; padding:.8em; ">
                                                <span style="font-size:16pt;  font-family: 'Cambria','times new roman','garamond',serif; color:#ff0000;">{% trans "Disclaimer" %}</span><br/>
                                                <p style="font-size:11pt; line-height:10pt; font-family: 'Cambria','times roman',serif;">{{ system_settings.disclaimer }}</p>
                                            </div>
                                        {% endif %}
								</p>
								</p>
								{% if url is not None %}
									<br/>
									<br/>
									More information on this event can be found here:
								{% endif %}
								<br/>
								</p>
                                {% blocktranslate trimmed with event_url=url|full_url %}
								<center><a href="{{event_url}}" class="proton-button" target="_blank">Go Risk Acceptance</a></center>
                                {% endblocktranslate %}
							</div>
						</td>
					</tr>
					<tr class="proton-tr">
						<td class="proton-td" colspan="10" style="">
							<div class="body-margin">
								<h3>{% trans "Regards" %}</h3><br/>
									<p>Devsecops</p>
							</div>
						</td>
					</tr>

					<tr class="proton-tr">
						<td class="proton-td" colspan="10" style="">
							<div class="proton-divider"></div>
							<center>
								<span style="color: #00000"> © 2024 Devsecops Engine </span>
							</center>
							<div class="proton-margin-bottom"></div>
						</td>
					</tr>
                    {% endautoescape %}
				</tbody>
			</table>
		</div>
	</body>
</html>