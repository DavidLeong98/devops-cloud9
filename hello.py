import click
import boto3


def add(x,y):
    return x+y

@click.command()
def buckets():
    """"This is  my AWS s3 bucket """
    
    s3 = boto3.client("s3")
    all_buckets = s3.list_buckets()
    for bucket in all_buckets["Buckets"]:
        click.echo(
            click.style(f"bucket: {bucket['Name']}", bg="yellow" , fg = "blue")
            )
        
        
if __name__ == "__main__":
    buckets()