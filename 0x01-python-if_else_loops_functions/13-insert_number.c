#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node in a sorted list
 * @head: head of the list
 * @number: number to add
 * Return: addres of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new;

	if (number <= (*head)->n)
	{
		new = malloc(8);
		if (!new)
		{
			return (NULL);
		}
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	aux = *head;
	while (aux->next)
	{
		if (number <= aux->next->n)
		{
			new = malloc(8);
			if (!new)
				return (NULL);
			new->n = number;
			new->next = aux->next;
			aux->next = new;
			return (new);
		}
		aux = aux->next;
	}
	new = malloc(8);
	if (!new)
		return (NULL);
	new->n = number;
	aux->next = new;
	return (new);
}
