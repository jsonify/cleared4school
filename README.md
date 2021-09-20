# cleared4school
 
## About
Python script to run either manually or as a crontab job that will log a user into the [[Cleared4School]](https://app.cleared4school.com/login) student attestation application to attest that the student has shown no signs of the various issues that would prevent a student from being cleared to attend school for the day.

## Script Installation

```bash
git clone https://github.com/jsonify/cleared4school
cd cleared4school
```

## Script Usage

## Dependencies

### Environment Variables

For manual execution, these need to be added to the `.zshrc` profile, and to run with a ***crontab*** job, these currently have to be passed inline in job execution statement

```
C4S_LOGIN
C4S_PASS
GMAIL_EMAIL
GMAIL_PASS
```

***.zshrc***

Generally located at `~/.zshrc`

```
export C4S_LOGIN="[your cleared4school username]"
export C4S_PASS="[your cleared4school password]"
export GMAIL_EMAIL="[your gmail email]"
export GMAIL_PASS="[your gmail password]"
export TXTADDRESS="[your mobile carrier's text message address]"
```

After the file has been updated with the desired variables, run `source ~/.zshrc` to refresh the session. VS Code should be restarted if editing through there.

***crontab job example***

```
0 9 * * * GMAIL_PASS="[your gmail password]" GMAIL_EMAIL="[your gmail email]" C4S_PASS="[your cleared4school password]" C4S_LOGIN="[your cleared4school username]" path/to/python ath/to/script > path/to/log/for/debugging 2>&1
```

## FAQ

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Feedback
If you find a bug / want a new feature to be added, please [open an issue](https://github.com/jsonify/cleared4school/issues).

## License
[MIT](https://choosealicense.com/licenses/mit/)