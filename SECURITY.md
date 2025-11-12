# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < Latest| :x:                |

We recommend always using the latest version of ToolsForImage to ensure you have the most up-to-date security patches.

## Reporting a Vulnerability

We take the security of ToolsForImage seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please Do Not

- **Do not** open a public GitHub issue for security vulnerabilities
- **Do not** disclose the vulnerability publicly until we've had a chance to address it
- **Do not** exploit the vulnerability beyond what is necessary to demonstrate it

### Please Do

1. **Email us**: Send details to burstneuron1729@gmail.com
2. **Include details**: Provide as much information as possible about the vulnerability:
   - Type of vulnerability (e.g., XSS, SQL injection, etc.)
   - Full paths of source file(s) related to the vulnerability
   - Location of the affected source code (tag/branch/commit or direct URL)
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the issue, including how an attacker might exploit it

3. **Allow time for a fix**: Give us reasonable time to investigate and fix the issue before public disclosure

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Regular updates**: We will send you regular updates about our progress
- **Credit**: If you wish, we will publicly credit you for the discovery once the fix is released
- **Timeline**: We aim to release a fix within 90 days of the initial report

## Security Best Practices for Users

When deploying ToolsForImage:

1. **Environment Variables**: Never commit `.env` files with sensitive information
2. **HTTPS**: Always use HTTPS in production environments
3. **Updates**: Keep all dependencies up to date
4. **File Uploads**: Configure appropriate file size limits and validation
5. **Access Control**: Implement appropriate authentication if deploying publicly
6. **Input Validation**: The application validates inputs, but always sanitize on your end as well
7. **Rate Limiting**: Consider implementing rate limiting for public deployments

## Known Security Considerations

- **File Processing**: This application processes user-uploaded images. While we validate file types, always deploy behind proper security measures
- **Client-Side Processing**: Some image processing happens client-side in the browser for privacy and performance
- **No Data Storage**: By design, we don't store uploaded images, but ensure your deployment maintains this privacy standard

## Security Updates

Security updates will be released as soon as possible after a vulnerability is confirmed. Check the [releases page](https://github.com/mlbrothers/ToolsForImage-OSS/releases) for security announcements.

## Bug Bounty Program

We currently do not offer a bug bounty program, but we deeply appreciate responsible disclosure and will acknowledge your contribution.

## Questions

If you have questions about this security policy, please contact us at burstneuron1729@gmail.com.

---

Last updated: 2025-11-12
