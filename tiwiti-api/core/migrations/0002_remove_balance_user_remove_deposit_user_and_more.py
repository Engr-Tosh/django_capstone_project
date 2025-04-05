# Generated by Django 5.1.6 on 2025-04-03 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transactionlog',
            name='deposit_transaction',
        ),
        migrations.DeleteModel(
            name='PersonalUsage',
        ),
        migrations.DeleteModel(
            name='TotalBalance',
        ),
        migrations.RemoveField(
            model_name='transactionlog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transactionlog',
            name='withdrawal_transaction',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Balance',
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='TransactionLog',
        ),
        migrations.DeleteModel(
            name='Withdrawal',
        ),
    ]
