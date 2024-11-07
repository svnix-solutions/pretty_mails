
import frappe
from frappe.email.doctype.email_account.email_account import EmailAccount
from frappe.utils import (
	get_url,
	scrub_urls,
)

from frappe.email.email_body import get_header, get_footer, get_brand_logo, inline_style_in_html
from frappe.email import email_body

def pretty_mails_get_formatted_html(
	subject,
	message,
	footer=None,
	print_html=None,
	email_account=None,
	header=None,
	unsubscribe_link: frappe._dict | None = None,
	sender=None,
	with_container=False,
):

	email_account = email_account or EmailAccount.find_outgoing(match_by_email=sender)

	rendered_email = frappe.get_template("pretty_mails/templates/emails/standard.html").render(
		{
			"brand_logo": get_brand_logo(email_account) if with_container or header else None,
			"with_container": with_container,
			"site_url": get_url(),
			"header": get_header(header),
			"content": message,
			"footer": get_footer(email_account, footer),
			"title": subject,
			"print_html": print_html,
			"subject": subject,
		}
	)

	html = scrub_urls(rendered_email)

	if unsubscribe_link:
		html = html.replace("<!--unsubscribe link here-->", unsubscribe_link.html)

	return inline_style_in_html(html)

email_body.get_formatted_html = pretty_mails_get_formatted_html